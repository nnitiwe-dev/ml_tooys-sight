# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    path('cv/', include('computervision.urls')),
]



