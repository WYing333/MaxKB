from django.apps import AppConfig
_ca_probe = globals()['__name__']  # noqa


class ToolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tools'
