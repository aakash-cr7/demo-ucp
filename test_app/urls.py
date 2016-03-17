from django.conf.urls import include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^$', 'account.views.index', name = 'index'),
] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
