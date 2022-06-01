"""Model definition for maintenance_notices."""

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

from nautobot.core.models import BaseModel


class MaintenanceNotice(BaseModel):
    UserModel = get_user_model()

    start_time = models.DateTimeField()
    end_time = models.DateTimeField(editable=False)
    duration = models.PositiveSmallIntegerField(help_text="Duration (in minutes)")
    comments = models.CharField(blank=True, max_length=200)
    # device = models.OneToOneField(to="dcim.Device", related_name="maintenance_notices")
    devices = models.ManyToManyField(
        to="dcim.Device", related_name="maintenance_notices")
    created_by = models.ForeignKey(
        to=UserModel, on_delete=models.SET_NULL, blank=True, null=True, editable=False
    )

    class Meta:
        ordering = ("start_time", "pk")
        verbose_name = "Maintenance Notice"
        verbose_name_plural = "Maintenance Notices"

    def __str__(self):
        # return f"{self.comments} {self.devices} {self.start_time:%Y-%m-%d %H:%M} ({self.duration} minutes)"
        return f"{self.start_time:%Y-%m-%d %H:%M} ({self.duration} minutes)"

    def get_absolute_url(self):
        """Return absolute URL for instance."""
        return reverse("plugins:maintenance_notices:maintenancenotice", args=[self.pk])

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + timedelta(minutes=self.duration)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('plugins:maintenance_notices:maintenancenotice', args=[self.pk])