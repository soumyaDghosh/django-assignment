import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(instance, created, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal received for: {instance.name} in thread: {current_thread}")

def create_instance():
    current_thread = threading.current_thread().name
    print(f"Creating instance in thread: {current_thread}")
    obj = MyModel(name="Test Object")
    obj.save()

create_instance()
