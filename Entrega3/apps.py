from django.apps import AppConfig

class Entrega3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Entrega3'

    def ready(self):
        import Entrega3.signals  # 👈 IMPORTANTE
