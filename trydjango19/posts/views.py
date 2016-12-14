from django.http import HttpResponse
from django.shortcuts import render


def post_create(request):
    return HttpResponse("<h1>Create</>")


def post_detail(request):
    return HttpResponse("<h1>Detail</>")


def post_list(request):
    return render(request, "index.html", {})


def post_update(request):
    return HttpResponse("<h1>Update</>")


def post_delete(request):
    return HttpResponse("<h1>Delete</>")