from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_visualizar_catalogo_permission(sender, instance, created, **kwargs):
    if created:
        # Asignar el permiso 'visualizar_catalogo' al usuario
        permission = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permission)

        print("Permiso 'visualizar_catalogo' asignado correctamente al nuevo usuario.")
