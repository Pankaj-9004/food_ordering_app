from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from .models import *
from django.contrib import messages
from cart.cart import Cart
import razorpay

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/restro/login")
def homepage(request):
    cat = Category.objects.all()
    catid = request.GET.get("category")
    if catid:
        pro = Meal.objects.filter(category=catid)
    else:
        pro = Meal.objects.all().order_by('date_created')
    return render(request, "homepage.html", {'pro': pro, 'cat': cat})

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/restro/homepage')
    form = NewUserForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/restro/homepage/')
    form = CustomAuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required(login_url="/restro/login")
def signout(request):
    logout(request)
    return redirect('/restro/signin')

@login_required(login_url="/restro/login")
def update_profile(request):
    if request.method == 'POST':
        u_form = updateform(request.POST, instance=request.user)
        p_form = profileform(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your profile has been update')
            return redirect('/restro/profile')
    else:
        u_form = updateform(instance=request.user)
        p_form = profileform(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'update_profile.html', context)

@login_required(login_url="/restro/login")
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def meal_detail(request, pk):
    meal = Meal.objects.filter(id=pk)
    return render(request, 'meal_detail.html', {'meal': meal})

@login_required(login_url="/restro/signin")
def cart_add(request, id):
    cart = Cart(request)
    product = Meal.objects.get(id=id)
    cart.add(product=product)
    return redirect("/restro/homepage/")


@login_required(login_url="/restro/signin")
def item_clear(request, id):
    cart = Cart(request)
    product = Meal.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/restro/signin")
def item_increment(request, id):
    cart = Cart(request)
    product = Meal.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/restro/signin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Meal.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/restro/signin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'cart_detail.html')


def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart')
        user = request.user
        address = request.POST.get('address')
        state = request.POST.get('state')
        mobile_no = request.POST.get('mobile_no')
        zipcode = request.POST.get('zipcode')

        for i in cart:
            a = int(cart[i]['price'])
            b = cart[i]['quantity']
            total = a * b
            order = Order(
                user=user,
                meal=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                state=state,
                mobile_no=mobile_no,
                zipcode=zipcode,
                total=total,
            )
            order.save()
        request.session['cart'] = {}
        return redirect('/restro/homepage/')
    form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

client = razorpay.Client(auth = ('rzp_test_jevOXcHfNGLzoM', 'B4qADr8qYKXAkeUYXnpRZwWC'))
@login_required(login_url='/restro/signin/')
def payment(request):
    data = {"amount": 500, "currency": "INR", "payment_capture": "1"}
    payment = client.order.create(data=data)
    payment_id = payment['id']
    return render(request, 'payment.html', {'api_key': 'rzp_test_jevOXcHfNGLzoM', 'id': payment_id})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')




# 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