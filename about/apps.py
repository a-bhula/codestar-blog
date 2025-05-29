from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the About application.
    This class is used to set application-specific settings and metadata.
    It inherits from `django.apps.AppConfig` and defines the name of the application
    and the default auto field type for model primary keys.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
