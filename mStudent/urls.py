
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "mStudent Staff Dashboard"
admin.site.site_title = "mStudent"
admin.site.index_title = 'Dashboard'


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', admin.site.urls),


]
