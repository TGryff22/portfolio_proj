from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from breeds.models import Breed
from breeds.serializers import BreedSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "breeds/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Breed.objects.all()
    return render(request, "breeds/index.html", {"breeds": queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "breeds/index.html"

    def get(self, request):
        queryset = Breed.objects.all()
        return Response({"breeds": queryset})


class list_all_breeds(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "breeds/breed_list.html"

    def get(self, request):
        queryset = Breed.objects.all()
        return Response({"breeds": queryset})


# Create your views here.
@api_view(["GET", "POST", "DELETE"])
def breed_list(request):
    if request.method == "GET":
        tutorials = Breed.objects.all()

        title = request.GET.get("title", None)
        if title is not None:
            breeds = breeds.filter(title__icontains=title)

        breeds_serializer = BreedSerializer(tutorials, many=True)
        return JsonResponse(breeds_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "POST":
        breed_data = JSONParser().parse(request)
        breed_serializer = BreedSerializer(data=breed_data)
        if breed_serializer.is_valid():
            breed_serializer.save()
            return JsonResponse(breed_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(breed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        count = Breed.objects.all().delete()
        return JsonResponse(
            {"message": "{} Breeds were deleted successfully!".format(count[0])},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def breed_detail(request, pk):
    try:
        tutorial = Breed.objects.get(pk=pk)
    except Breed.DoesNotExist:
        return JsonResponse(
            {"message": "The breed does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        breed_serializer = BreedSerializer(breed)
        return JsonResponse(breed_serializer.data)

    elif request.method == "PUT":
        breed_data = JSONParser().parse(request)
        breed_serializer = BreedSerializer(tutorial, data=breed_data)
        if breed_serializer.is_valid():
            breed_serializer.save()
            return JsonResponse(breed_serializer.data)
        return JsonResponse(breed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        breed.delete()
        return JsonResponse(
            {"message": "Breed was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def breed_list_published(request):
    breeds = Breed.objects.filter(published=True)

    if request.method == "GET":
        breeds_serializer = BreedSerializer(breeds, many=True)
        return JsonResponse(breeds_serializer.data, safe=False)
