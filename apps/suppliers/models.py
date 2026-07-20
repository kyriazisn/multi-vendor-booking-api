from django.conf import settings
from django.db import models


class Supplier(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="supplier_profile"
    )
    business_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name