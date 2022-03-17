from django.contrib import admin
from django.urls import path
from test1.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index)
]