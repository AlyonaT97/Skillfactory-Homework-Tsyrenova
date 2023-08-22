from django.core.mail import mail_managers
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post

@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'
    else:
        subject = f'Appointment change for {instance.client_name} {instance.date.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )
    print(f'{instance.client_name} {instance.date.strftime("%d %m %Y")}')