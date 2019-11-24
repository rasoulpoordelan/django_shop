from django.urls import path
from . import views


urlpatterns = [
    path("category/",views.CategoryList.as_view()),
    path("product/",views.get_products)
]

