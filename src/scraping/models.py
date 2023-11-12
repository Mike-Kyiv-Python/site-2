from django.db import models

class city(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва міста', unique=True)
    slug = models.CharField(max_length=50, blank=True, verbose_name='SEO URL', unique=True)

    class Meta:
        verbose_name = 'Назва міста'
        verbose_name_plural = 'Назви міст'

    def __str__(self):
        return self.name


