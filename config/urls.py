from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # Django admin
  path('admin/', admin.site.urls),

  # User management
  path('accounts/', include('allauth.urls')), 
  path('', include('users.urls')),

  # Local apps
  path('', include('pages.urls')),
  path('', include('blog.urls')),
  path('api/v1/', include('api.urls')),
] + static(
  settings.MEDIA_URL,
  document_root=settings.MEDIA_ROOT
)
# since user-uploaded media exists in production environment,
# need to update urls to show files locally
