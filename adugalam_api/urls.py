from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin-panel/", include("admin_panel.urls")),
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/turfs/", permanent=False)),
    path("turfs/", include("turfs.urls")),
    path("booking/", include("bookings.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
