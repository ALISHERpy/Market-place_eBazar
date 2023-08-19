from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('users/', include("users.urls")),
    path('api/', include("api.urls")),
    path('users/', include('django.contrib.auth.urls')),
    path("products/", include('products.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

