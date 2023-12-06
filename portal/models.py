from django.db import models

# Create your models here.
class InstallerDetail(models.Model):
    installer_vorname = models.CharField(max_length=60)
    installer_nachname = models.CharField(max_length=60)
    installer_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.installer_vorname} {self.installer_nachname}"

class CompanyDetail(models.Model):
    company_name = models.CharField(max_length=60)
    installer_partner_cmy_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.company_name}"
