from django.urls import reverse


def user_detail_url(email):
    return reverse("user-detail", args=[email])
