from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FIMALE = 'F', 'Fimale'
        OTHERS = 'O', 'Others'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.png', upload_to='profiles')
    bio = models.TextField(blank=True, default='Update your Bio...')
    phone_number = models.CharField(max_length=13, default='+555895234')
    married = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GenderChoices,
                              default=GenderChoices.MALE)

    def __str__(self) -> str:
        return self.user.username

    def save(self, *args, **kwargs):
        #  Save the image first
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        if image.width > 300 or image.height > 300:
            output_size = (100, 100)
            image.thumbnail(output_size)
            # Overwrite the saved image.
            image.save(self.image.path)
