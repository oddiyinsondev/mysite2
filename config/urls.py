from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import Postlist, post_detail, registertion, logoutUser, loginUser, category_post, ContactUser, about, shohruhbek

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('oddiyinsondev/', admin.site.urls),
    # path('', include('blog.ulrs'))
    path('api/v1/', include('api.urls')),
    path('contact/', ContactUser, name="contact" ),
    path('', Postlist.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name="post_detail"),
    path('register/', registertion, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('about/', about, name='about'),
    path('login/', loginUser, name='login'),
    path('category/<slug:slug>/', category_post, name='category_post'),
    path('shohruhbek/', shohruhbek, name='shohruhbek' ),
    path('api-auth/', include('rest_framework.urls'))
]

handler404 = 'blog.views.pag_not'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)