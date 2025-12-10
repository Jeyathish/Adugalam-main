from django.urls import path
from .views import (
    add_turf,
    turf_list,
    turf_detail,
    upload_turf_image,
    delete_turf_image,
    edit_turf,
    turf_search,
    turf_slots_by_date,
)

urlpatterns = [
    # PUBLIC TURF APIs
    path("", turf_list),                                      # GET /turfs/
    path("search/", turf_search),                             # GET /turfs/search/
    path("<int:turf_id>/slots/", turf_slots_by_date),         # GET /turfs/5/slots/
    path("<int:turf_id>/", turf_detail),                      # GET /turfs/5/

    # OWNER TURF APIs
    path("add/", add_turf),
    path("<int:turf_id>/edit/", edit_turf),
    path("<int:turf_id>/upload-image/", upload_turf_image),
    path("image/<int:image_id>/delete/", delete_turf_image),
]

