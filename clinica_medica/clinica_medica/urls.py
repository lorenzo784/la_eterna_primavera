
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuenta/', include('cuenta.urls', namespace='cuenta')),
    path('', include('pagina.urls', namespace='pagina')),
]
