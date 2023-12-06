from django.shortcuts import render, get_object_or_404
from .models import TimeRelatedDetail


# creating function based views
def time_related_detail_view(request, installer_id):
    time_related_detail = get_object_or_404(TimeRelatedDetail, installer__id=installer_id)
    context = {
        'installer_id': installer_id,
        'time_related_detail': time_related_detail
    }
    return render(request, "timeapp/time_related.html", context)
