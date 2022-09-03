from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core app
    path('', include('core.urls', namespace='core')),
]
