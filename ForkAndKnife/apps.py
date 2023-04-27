from django.apps import AppConfig


class ForkandknifeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ForkAndKnife"

def myFunction(name):
    print(name);