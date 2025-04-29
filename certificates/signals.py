# diplomtest/certificates/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CertificatesCertificate
from journals.models import JournalsJournalregistration

@receiver(post_save, sender=CertificatesCertificate)
def create_journal_registration(sender, instance, created, **kwargs):
    if created:
        JournalsJournalregistration.objects.create(
            si=instance.si,
            receipt_date=instance.verification_date,
            receipt_signature=instance.verifier.get_full_name() or instance.verifier.username
        )