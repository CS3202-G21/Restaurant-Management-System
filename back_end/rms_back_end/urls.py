from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('rooms.urls')),
    path('', include('restaurants.urls')),
    path('', include('menu_items.urls')),
    path('', include('special_offers.urls')),
    path('', include('customers.urls')),
    path('', include('staff.urls')),
    path('', include('room_reservations.urls')),
<<<<<<< HEAD
=======
    path('', include('table_reservations.urls')),
>>>>>>> 7b6ec6af1e35b280ef8349566087930c3aeb455f
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
