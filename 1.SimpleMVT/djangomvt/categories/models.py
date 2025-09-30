import os
import uuid
from io import BytesIO
from django.core.files.base import ContentFile
from slugify import slugify  # це з python-slugify

from PIL import Image
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null = True, blank = True)

    image = models.ImageField(upload_to='categories/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old = type(self).objects.filter(pk=self.pk).first()
        else:
            old = None

        # Якщо зображення нове або змінене
        if self.image and (not old or old.image != self.image):
            # Якщо вже є фото (старе), видаляємо перед збереженням нового
            if old and old.image and old.image != self.image:
                old.image.delete(save=False)

            img = Image.open(self.image)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            filename = f"{uuid.uuid4().hex}.webp"
            buffer = BytesIO()
            img.save(buffer, format='WEBP')
            buffer.seek(0)
            self.image.save(filename, ContentFile(buffer.read()), save=False)
        elif old and old.image and not self.image:
            # Якщо зображення було видалено
            old.image.delete(save=False)

        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug



        super().save(*args, **kwargs)

    # String representation of the model
    def __str__(self):
        return self.name
