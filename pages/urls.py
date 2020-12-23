from django.urls import path
from .views import PageListView, PageDetailView

urlpatterns = [
    path("page/<int:pk>/", PageDetailView.as_view(), name="detail_page"),
    path("", PageListView.as_view(), name="home"),
]
