from django.db import models
from django.conf import settings
from uuid import uuid4

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return str(self.title)


