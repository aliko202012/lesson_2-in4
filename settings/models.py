from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Имя сотрудника'
    )
    description = models.TextField(
        verbose_name='Описание сотрудника  '
    )
    logo = models.ImageField(
        upload_to='logo_image/'
    )