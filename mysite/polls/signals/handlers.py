from django.db.models.signals import pre_save
from django.dispatch import receiver
from polls.models import Question

from polls.signals.senders import custom_signal

@receiver(pre_save, sender=Question)
def my_handler(sender, **kwargs):
  print("pre_save handler called")

@receiver(custom_signal)
def my_custom_handler(sender, **kwargs):
  print("custom_handler called")