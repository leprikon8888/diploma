from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Port(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='ports/', blank=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Portfolio, on_delete=models.PROTECT, related_name='ports')


class BrandShapka(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Poslugi(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField(max_length=800, unique=True)
    span = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'