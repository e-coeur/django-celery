from django.conf.urls import include, url

from acc import views

urlpatterns = [
    url(r'profile/$', views.CustomerProfile.as_view(), name='profile'),
    url('', include('django.contrib.auth.urls')),
    url('', include('social_django.urls', namespace='social')),
]
