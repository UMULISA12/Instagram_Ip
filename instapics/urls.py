from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url(r'^$', views.instaImages, name='instaImages'),
    # url(r'^instaImages', views.instaImages, name='welcome'),

    url(r'^what_profile/(?P<profile_id>\d+)', views.my_profile, name='profile'),
    url(r'^explore_more/', views.explore, name='my_explore'),
    url(r'^new/image$', views.new_image, name='new-image'),

]
