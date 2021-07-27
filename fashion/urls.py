from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$' , views.get_images , name= 'homepage'),
    url('^user/' , views.userpage , name= 'username') ,
    
]