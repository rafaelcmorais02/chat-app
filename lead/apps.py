from django.apps import AppConfig


class LeadConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lead"

    def ready(self) -> None:
        # flake8: noqa: F401
        import lead.signals
        return super().ready()
