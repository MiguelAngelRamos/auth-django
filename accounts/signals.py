from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

# Esta funcion se va ejecutar cuando reciba la señal
@receiver(post_save, sender=Profile)
def add_user_group(sender, instance, created, **kwargs):
    if created:
        try:
            users_group = Group.objects.get(name='admin')
        except Group.DoesNotExist:
            # users_group = Group.objects.create(name='users')
            users_group = Group.objects.create(name='admin')
            
        instance.user.groups.add(users_group)
    