from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^aboutus/$', views.aboutus, name="aboutus"),
    url(r'^security/$', views.security, name="security"),
    url(r'^webdev/$',views.webdev, name="webdev"),
    url(r'^programming/$', views.programming, name="programming"),
    url(r'^networking/$', views.networking, name="networking"),
    url(r'^artificialintelligence/$', views.artificialintelligence, name="artificialintelligence"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
