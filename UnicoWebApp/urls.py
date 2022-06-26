from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members_app.urls')),
]

admin.site.site_header = "Unico Web App"
admin.site.site_title = "Unico Web App"
