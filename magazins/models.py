from django.db import models
from django.db.models import CharField, TextField, SlugField, ForeignKey, DO_NOTHING
from django.utils.text import slugify


# Create your models here.
class Publicatie(models.Model):
    class Meta:
        verbose_name_plural = 'Publicatii'

    name = CharField(max_length=100)

    def __str__(self):
        return self.name

class Revista(models.Model):
    class Meta:
        verbose_name_plural = 'Reviste'

    title = CharField(max_length=100)
    description = TextField()
    slug = SlugField(unique=True, editable=False)
    publicatie = ForeignKey(Publicatie, on_delete=DO_NOTHING)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
