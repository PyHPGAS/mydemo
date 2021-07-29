from django.apps import AppConfig


class PicklistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PickList'
    verbose_name = 'Pick List'
    icon_name = 'person'
    # label = 'Pick.PickList'