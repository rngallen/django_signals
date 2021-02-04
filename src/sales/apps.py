from django.apps import AppConfig


class SalesConfig(AppConfig):
    name = 'sales'

    def ready(self) -> None:
        import sales.signals
        return super().ready()
