from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("manpower/", include("manpower.urls")),
    path("plan/", include("plan.urls")),
    path("report/", include("report.urls")),
    path("test/", include("tests.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)