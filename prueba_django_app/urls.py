from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('tienda/', views.tienda, name='tienda'),
    path('contacto/', views.contacto, name='contacto'),
    path('blog/', views.blog, name='blog'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
