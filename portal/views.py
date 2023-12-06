from django.shortcuts import render, get_object_or_404
from .models import InstallerDetail, CompanyDetail


# Creating function based views
def installer_company_detail_view(request, installer_id, company_id):
    installer = get_object_or_404(InstallerDetail, pk=installer_id)
    company = get_object_or_404(CompanyDetail, pk=company_id)
    context = {
        'installer': installer,
        'company': company
    }
    return render(request, "portal/installer_and_company_detail.html", context)


# def company_detail_view(request, company_id):
#     company = get_object_or_404(CompanyDetail, pk=company_id)
#     return render(request, "portal/installer_and_company_detail.html", {'company': company})
