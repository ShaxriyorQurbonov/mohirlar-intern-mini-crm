from django.db import models

import uuid

from django.contrib.auth.models import User


class Lead(models.Model):

    class Status(models.TextChoices):
        NEW = "NEW", "new",
        CONTACTED = "CONTACTED","contacted",
        QUALIFIED = "QUALIFIED", "qualified",
        WON = "WON" , "won",
        LOST = "LOST", "lost"

    class Source(models.TextChoices):
        INSTAGRAM = "INSTAGRAM", "Instagram"
        TELEGRAM = "TELEGRAM", "Telegram"
        WEBSITE = "WEBSITE", "Website"
        FACEBOOK = "FACEBOOK", "Facebook"
        REFERRAL = "REFERRAL", "Referral"
        OTHER = "OTHER", "Other"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False,
    )

    name = models.CharField(max_length=150)

    email = models.EmailField(
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    source = models.CharField(
        max_length=20,
        choices=Source.choices,
        default=Source.OTHER,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    note = models.TextField(blank=True,)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="leads",
    )

    created_at = models.DateTimeField(auto_now_add=True,)

    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.name
