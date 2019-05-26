from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    FirstNameSerializer,
    LastNameSerializer,
    RegisterWorkerSerializer,
)
from .models import FirstName, LastName, RegisterWorker
from .tasks import register_worker


def print_hello(request):
    register_worker.delay()
    return HttpResponse("hello")


# Create your views here.
class RegisterApi(APIView):
    serializer_class_first_name = FirstNameSerializer
    serializer_class_last_name = LastNameSerializer
    serializer_class_register_worker = RegisterWorkerSerializer

    serializer_class = RegisterWorkerSerializer

    def get_queryset_first_name(self):
        return FirstName.objects.all()

    def get_queryset_last_name(self):
        return LastName.objects.all()

    def get_queryset_worker(self):
        return RegisterWorker.objects.first()

    def get(self, request):
        first_names = self.serializer_class_first_name(
            self.get_queryset_first_name(), many=True
        )
        last_names = self.serializer_class_last_name(
            self.get_queryset_last_name(), many=True
        )
        register_settings = self.serializer_class_register_worker(
            self.get_queryset_worker(), many=False
        )
        return Response(
            {
                "firstNamePool": first_names.data,
                "lastNamePool": last_names.data,
                "register": register_settings.data,
            }
        )

