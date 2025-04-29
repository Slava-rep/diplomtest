# diplomtest/si/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SiAffectingfactors
from journals.models import JournalsJournalenvironment

@receiver(post_save, sender=SiAffectingfactors)
def create_journal_environment(sender, instance, created, **kwargs):
    if created:
        JournalsJournalenvironment.objects.create(
            affecting_factors=instance
        )