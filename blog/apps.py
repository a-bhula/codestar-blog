from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the Blog application.
    This class is used to set application-specific settings and metadata.
    It inherits from `django.apps.AppConfig` and defines the name of the application
    and the default auto field type for model primary keys.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
