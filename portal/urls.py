from .views import installer_company_detail_view
from django.urls import path

urlpatterns = [
    path("installer/", installer_company_detail_view, name="installer_related"),
    # path("company/<int:company_id>/", views.company_detail_view, name="company_related")
]
