from django.contrib import admin
from django.urls import path,include
from groups import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('telegram',views.telegram,name="telegram"),
    path('whatsapp',views.whatsapp,name="whatsapp"),
    path('contact',views.contact,name="contact"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
