from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def ecommerce_index(request):
    return HttpResponse("Welcome to the shop!")


def get_user(request, user_name):
    user_data = {
        "user_id": user_name,
        "email": f"{user_name}@exmaple.com",
        "createdAt": "2021-09-01T00:00:00Z",
    }

    return JsonResponse(user_data)


def get_allProduct(request):
    products = [
        {
            "product_id": 1,
            "product_name": "Black Tee",
            "price": 100,
        },
        {"product_id": 2, "product_name": "Sneaker", "price": 300},
        {"product_id": 3, "product_name": "Slack", "price": 500},
    ]

    return JsonResponse({"products": products})


def getProductById(request, product_id):
    products = [
        {
            "product_id": 1,
            "product_name": "Black Tee",
            "price": 100,
        },
        {"product_id": 2, "product_name": "Sneaker", "price": 300},
        {"product_id": 3, "product_name": "Slack", "price": 500},
    ]
    return JsonResponse(products[product_id - 1])


def get_comment_by_product(request, product_id):
    comments = [
        {
            "product_id": 1,
            "comment": [
                {"user_id": "user1", "comment": "good tee"},
                {"user_id": "user2", "comment": "too big"},
                {"user_id": "user3", "comment": "too small"},
            ],
        },
        {
            "product_id": 2,
            "comment": [
                {"user_id": "user1", "comment": "good sneaker"},
                {"user_id": "user2", "comment": "too big"},
                {"user_id": "user3", "comment": "bad durability"},
            ],
        },
        {
            "product_id": 3,
            "comment": [
                {"user_id": "user1", "comment": "good slack"},
                {"user_id": "user2", "comment": "too big"},
                {"user_id": "user3", "comment": "leg is too long"},
            ],
        },
    ]

    try:
        return JsonResponse({"comments": comments[product_id - 1]["comment"]})
    except IndexError:
        return JsonResponse({"error": "Product not found"}, status=404)


def shop_summarize(reqeust):
    shop_data = {
        "total_products": 3,
        "total_users": 3,
        "total_comments": 9,
        "total_order": 50,
    }

    return JsonResponse(shop_data)
