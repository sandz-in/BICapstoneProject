from django.template.context_processors import csrf

from django.shortcuts import render


# Create your views here.
from recommendation.bi_knn import knn_recommender


def home_view(request):
    context = {}
    context.update(csrf(request))
    url_image = request.POST.get("url")
    if url_image is not None and url_image != "":
        result = knn_recommender(url_image)
        print result
        context["result"] = result
        context["url_image"] = url_image
    return render(request, 'index.html', context)
