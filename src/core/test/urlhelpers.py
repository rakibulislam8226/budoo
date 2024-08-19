from django.urls import reverse


def user_list_url():
    return reverse("user-list")


def user_detail_url(email):
    return reverse("user-detail", args=[email])
