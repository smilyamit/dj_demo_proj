from django.urls import path
from . import views

urlpatterns = [
    path("time_related/<int:installer_id>/", views.time_related_detail_view, name="time_detail"),
    # path("time_related/<int:installer_id>/", views.TimeRelatedDetail, name="time_detail")  #this is wrong it should take function from views not from model
]
