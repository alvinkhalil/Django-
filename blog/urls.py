from blog import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from article import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('articles/',include("article.urls"),name = "articles"),
    path("user/", include("user.urls"), name="user")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

