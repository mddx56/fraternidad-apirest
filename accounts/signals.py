from django.contrib.auth import get_user_model

# Signals import
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        # deuda = Deuda.objects.create(deuda_total=0, user=instance)
        # deuda.save()
        # print(f"user {instance.username}")
        print("SIGNAL ACCOUNT :", "crated..")
    else:
        print("SIGNAL ACCOUNT :", "update..")
