from django.contrib import admin
from django.urls import path, include
from main import views as main_views   # 👈 add this import


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),  # include app urls from "main"
    path('', main_views.dashboard, name='home'), # 👈 root URL → dashboard

]
