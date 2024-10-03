from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(instance, created, **kwargs):
    print(f"Signal received for: {instance.name}")

def create_instance():
    print("Creating instance...")
    obj = MyModel(name="Test Object")
    obj.save()

create_instance()
