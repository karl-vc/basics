"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#first we import the file name..this is the req page so the code we write in view has to be imported here

from firstapp import views
from django.conf.urls import url,include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^home/$',views.home),
    url(r'^user/',include('firstapp.urls')),
    url(r'^master/$',views.testhome),
    url(r'^signup/$',views.signup),
    url(r'^formname/$',views.formname),
    url(r'^viewdata/$',views.datafetch),
    url(r'^viewall/$',views.viewall),
    url(r'^viewone/$',views.viewone),
    url(r'^image/$',views.image),
    url(r'^update/$',views.update),
    url(r'^delete/$',views.deletedata),
    url(r'^edit/$',views.editdata),
    url(r'^imagefetch/$',views.imagefetch),
    url(r'^viewimage/$',views.viewimage),
    url(r'^viewimage2/$',views.viewimage2),
    url(r'^delete1/$',views.deleteimage),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
