from django.db import models

from portal.models import InstallerDetail


# Create your models here.
class TimeRelatedDetail(models.Model):
    installer = models.OneToOneField(InstallerDetail, on_delete=models.CASCADE)
    starting_date = models.DateField(null=True, blank=True)
    starting_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.installer.installer_vorname}"
