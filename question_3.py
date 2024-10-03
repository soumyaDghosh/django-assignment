from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

class LogEntry(models.Model):
    message = models.CharField(max_length=255)

@receiver(post_save, sender=MyModel)
def log_creation(instance, created, **kwargs):
    if created:
        LogEntry.objects.create(message=f"{instance.name} was created.")

def create_instance(should_fail=False):
    try:
        with transaction.atomic():
            obj = MyModel(name="Test Object")
            obj.save()
            
            if should_fail:
                raise ValueError("Simulated failure")
    except Exception as e:
        print(f"Error occurred: {e}")

create_instance()

print("LogEntries after first call:")
print(LogEntry.objects.all())

create_instance(should_fail=True)

print("LogEntries after second call:")
print(LogEntry.objects.all())

