from django.db import models
from django.contrib.auth.models import User # Es Modelo User que Django crea por defecto.
from django.db.models.signals import post_save
# Perfil del Usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/image_user_default.png', upload_to='users/', verbose_name="Imagen de Perfil")
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=150, null=True, blank=True, verbose_name='Teléfono')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']
        
    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)
