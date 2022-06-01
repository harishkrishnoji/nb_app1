from datetime import datetime, timezone
from django.test import override_settings
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
    def test_list_view(self):
        self.client.logout()
        response = self.client.get("/plugins/maintenance_notices/maintenancenotice/")
        self.assertHttpStatus(response, 200)