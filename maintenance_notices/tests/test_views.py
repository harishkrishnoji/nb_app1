from datetime import datetime, timezone
from django.test import override_settings
from django.urls import reverse
from nautobot.utilities.testing import ModelViewTestCase
from maintenance_notices import models

class TestMaintenanceNoticeViews(ModelViewTestCase):
    """Test Maintenance Notice Views."""

    model = models.MaintenanceNotice

    @classmethod
    def setUpTestData(cls):
        """Create two Maintenance Notices for view testing."""
        maintenance_1 = models.MaintenanceNotice.objects.create(start_time=datetime.now(timezone.utc), duration=30)
        maintenance_2 = models.MaintenanceNotice.objects.create(start_time=datetime.now(timezone.utc), duration=60)

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["maintenance_notices.maintenancenotice"])
    def test_list_view_anonymous(self):
        self.client.logout()
        path = reverse("plugins:maintenance_notices:maintenancenotice_list")
        response = self.client.get(path)
        self.assertHttpStatus(response, 200)
