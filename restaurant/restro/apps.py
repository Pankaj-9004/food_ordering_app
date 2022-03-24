from django.apps import AppConfig



class RestroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restro'

    def ready(self):
        from . import signals