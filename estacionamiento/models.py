from datetime import datetime
from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Perfil(models.Model):
    tipos = (('Propietario','Propietario'),
            ('Normal','Normal'))
    estado = (('Disponible','Disponible'),
            ('Ocupado','Ocupado'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50,blank=True,null=True,default='No se indica')
    telefono = models.PositiveIntegerField(blank=True,null=True)
    tipo = models.CharField(max_length=20,choices=tipos,default='Normal',null=True)
    latitud = models.FloatField(null=True,blank=True)
    longitud = models.FloatField(null=True,blank=True)
    foto = models.ImageField(upload_to='foto_estacionamiento/%Y/%m/%d', blank=True,null=True)
    estado = models.CharField(max_length=20,choices=estado,default='Normal',null=True)
@receiver(post_save, sender=User)
def create_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_perfil(sender, instance, **kwargs):
    instance.perfil.save()