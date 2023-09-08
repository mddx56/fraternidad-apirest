from django.contrib.auth import get_user_model

# Signals import
from django.dispatch import receiver
from django.db.models.signals import post_save
#from agendas.models import Extraordinaria,Deuda

User = get_user_model()

"""
@receiver(post_save, sender=Extraordinaria)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        #users = User.objects.all()
        extraord = instance
        deudas = Deuda.objects.all()
        
        #deuda.save()
        print(f"user {instance.username}")
    else:
        print("algo salio mal..")
"""