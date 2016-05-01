<<<<<<< HEAD
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
=======
from django.conf.urls import include, url
>>>>>>> 9fd0748a7995a1f445ae975cf4cfea51c8860cda
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newsletter.views.home', name='home'),
<<<<<<< HEAD
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
]

if settings.DEBUG:
 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    
]
>>>>>>> 9fd0748a7995a1f445ae975cf4cfea51c8860cda
