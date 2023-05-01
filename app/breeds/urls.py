from django.urls import path
from breeds import views as breeds_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', breeds_views.index, name='home'),
    path("", breeds_views.index.as_view(), name="home"),
    path("api/breeds/", breeds_views.breed_list),
    path("api/breeds/<int:pk>/", breeds_views.breed_detail),
    path("api/breeds/published/", breeds_views.breed_list_published),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
