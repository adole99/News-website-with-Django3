
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
    #path('',views.home,name='home'),
    path('',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('contact', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)