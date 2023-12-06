from django.shortcuts import render, get_object_or_404
from .models import InstallerDetail, CompanyDetail
from .forms import  InstallerDetailForm, CompanyDetailForm


def installer_company_detail_view(request):
    if request.method == 'POST':
        installer_form = InstallerDetailForm(request.POST)
        company_form = CompanyDetailForm(request.POST)

        if installer_form.is_valid() and company_form.is_valid():
            installer = installer_form.save(commit=False)
            installer.save()
            company = company_form.save(commit=False)
            company.save()

    else:
        installer_form = InstallerDetailForm()
        company_form = CompanyDetailForm()

    context = {
        'installer_form': installer_form,
        'company_form': company_form,
    }

    return render(request, "portal/installer_and_company_detail.html", context)

