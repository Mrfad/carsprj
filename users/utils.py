
# https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
def user_directory_path(instance, filename, profiles='profiles'):
    return f'{profiles}/user_{instance.user.id}/{filename}'