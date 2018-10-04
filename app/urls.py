from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.home,name = 'home'),
    url(r'^picture/(\d+)',views.image,name = 'picture'),
    url(r'^profile/(\w+)',views.profile,name = 'profile'),
    url(r'^edit/profile$',views.new_profile,name ='edit_profile'),
    url(r'^new/comment$',views.comment,name = 'new_comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)