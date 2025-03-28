"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from ecommerce import views as ecommerce_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ecommerce/", ecommerce_views.ecommerce_index),
    path("ecommerce/user/<user_name>", ecommerce_views.get_user),
    path("ecommerce/product/all", ecommerce_views.get_allProduct),
    path("ecommerce/product/ById/<int:product_id>", ecommerce_views.getProductById),
    path(
        "ecommerce/comment/ByProductId/<int:product_id>",
        ecommerce_views.get_comment_by_product,
    ),
    path("ecommerce/summarize", ecommerce_views.shop_summarize),
]
