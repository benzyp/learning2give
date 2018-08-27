"""
Definition of urls for Learning2Give.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

import app.forms
import app.views
import app.admin_views

from app.views import CauseViewSet

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from app import api_views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'causes',CauseViewSet)



urlpatterns = [
    url(r'^causes/$', app.api_views.cause_list),
    url(r'^causes/(?P<pk>[0-9a-zA-Z]+)/$', app.api_views.cause_detail),
    url(r'^students/$', app.api_views.student_list),
    url(r'^students/(?P<pk>[0-9a-zA-Z]+)/$', app.api_views.student_detail),
    url(r'^learners/$', app.api_views.learner_list),
    url(r'^learners/(?P<pk>[0-9a-zA-Z]+)/$', app.api_views.learner_detail),
    url(r'^donors/$', app.api_views.donor_list),
    url(r'^donors/(?P<pk>[0-9a-zA-Z]+)/$', app.api_views.donor_detail),
    url(r'^locations/$', app.api_views.locale_list),
    url(r'^locations/(?P<pk>[0-9a-zA-Z]+)/$', app.api_views.locale_detail),
    url(r'^sessions/$', app.api_views.session_list),
    url(r'^sessions/(?P<pk>[0-9a-zA-Z]+)/$', app.api_views.session_detail),

    url(r'^createTest/$', app.api_views.create_test),
    url(r'^/admin/causes/$', app.admin_views.admin_causes),


    #url(r'^causes$',app.views.get_causes, name='causes'),
    # rest_api
    url(r'^user-api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),

    url(r'^admin/causes', app.admin_views.admin_causes),
]
 