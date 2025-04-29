from django.db.models.signals import post_save
from django.dispatch import receiver
from certificates.models import Certificate
from si.models import AffectingFactors
from .models import JournalVerification, JournalEnvironment

# @receiver(post_save, sender=Certificate)
# def create_verification_journal(sender, instance, created, **kwargs):
#     if created:
#         JournalVerification.objects.create(
#             certificate=instance,
#             si=instance.si,
#             verification_result=instance.get_verification_result_display()
#         )

# @receiver(post_save, sender=AffectingFactors)
# def create_environment_journal(sender, instance, created, **kwargs):
#     if created:
#         JournalEnvironment.objects.create(affecting_factors=instance)

# diplomtest/journals/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from certificates.models import CertificatesCertificate
from .models import JournalsJournalverification

@receiver(post_save, sender=CertificatesCertificate)
def create_journal_verification(sender, instance, created, **kwargs):
    if created:
        JournalsJournalverification.objects.create(
            certificate=instance,
            si=instance.si,
            verification_result=instance.verification_result
        )