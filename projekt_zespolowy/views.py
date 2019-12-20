from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from models import gs_sync

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'office_status.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    gs_data = gs_sync()

    def get(self, request, format=None):
        labels = [v for v in range(0,11)]
        consumption = self.gs_data.get_curr_consumption()
        temp_out = self.gs_data.get_out_temp()
        temp_in = self.gs_data.get_ins_temp()
        is_airc_on = self.gs_data.is_airc_on()

        data = {
            "labels" : labels,
            "consumption" : consumption,
            "temp_out": temp_out,
            "temp_in": temp_in,
            "aircondition": is_airc_on
        }
        return Response(data)