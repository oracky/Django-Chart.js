from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'office_status.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["dsad", "gasda", "gasda"]
        hum = [12, 14, 21]
        data = {
            "labels" : labels,
            "humidity" : hum,
        }
        return Response(data)