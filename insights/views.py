from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WeeklyLossRecord
from .serializers import WeeklyLossSerializer

class WeeklyLossAPIView(APIView):
    def get(self, request):
        records = WeeklyLossRecord.objects.all()
        serializer = WeeklyLossSerializer(records, many=True)
        return Response({"weekly_loss_data": serializer.data})
