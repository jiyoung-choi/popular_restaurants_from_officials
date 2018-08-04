from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^djga/', include('google_analytics.urls')),
    url(r'^input_email$', views.input_email, name='input_email'),
    url(r'^dining_list$', views.dining_list, name='dining_list'),
    url(r'^dining_list_man$', views.dining_list, name='dining_list'),
    url(r'^dining_list_women$', views.dining_list, name='dining_list'),
]

GOOGLE_ANALYTICS = {
    'google_analytics_id': 'UA-123289484-1',
}
