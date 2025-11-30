from django.contrib import admin
from django.urls import path
from routing.views import TestView, RouteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", TestView.as_view()),
    path("api/route/", RouteView.as_view()),
]
