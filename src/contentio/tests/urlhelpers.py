from django.urls import reverse


def logs_list_url():
    return reverse("logs-list")


def logs_detail_url(uid):
    return reverse("logs-details", args=[uid])
