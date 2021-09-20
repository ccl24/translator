from . import views
from django.urls import path

urlpatterns = [
    # path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    # path('about/', views.AboutView.as_view(), name='about_view'),
    path('', views.translator_view, name='translator_view')     # form is a view, so no need for as_view() here.
]