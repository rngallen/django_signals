from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = "orders"

    def ready(self) -> None:
        import orders.signals

        return super().ready()
