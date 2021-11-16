from django.db import models

class PublishStateOptions(models.TextChoices):
    # constant = 'DB_Value', 'User_Display_value'
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'
    # UNLISTED = 'UN', 'Unlisted'
    # PRIVATE = 'PR', 'Private'