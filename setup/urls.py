
from django.contrib import admin
from django.urls import path, include

# Was imported the module include to be able to add the paths listed in 'galeria.urls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
    ]

