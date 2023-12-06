# portal/forms.py
from django import forms
from .models import InstallerDetail, CompanyDetail

class InstallerDetailForm(forms.ModelForm):
    class Meta:
        model = InstallerDetail
        fields = ["installer_vorname", "installer_nachname", "installer_id"]

class CompanyDetailForm(forms.ModelForm):
    class Meta:
        model = CompanyDetail
        fields = ["company_name", "installer_partner_cmy_id"]
