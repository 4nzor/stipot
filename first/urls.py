from django.contrib.auth.views import logout

from . import views
from django.conf.urls import url, include
urlpatterns = [

    url(r'^$', views.index, name='stipot'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^eventmap/$', views.eventmap, name = 'eventmap'),
    url(r'^faq/$', views.faq, name = 'faq'),
    url(r'^partners/$', views.partners, name = 'partners'),

    url(r'^signin/$', views.signin.as_view(), name = 'signin'),
    url(r'^register/$', views.register.as_view(), name = 'register'),
    
    url(r'^logout/$', logout, {'template_name': 'first/index.html'}),
    url(r'^account/$', views.profile, name = 'profile'),
]
