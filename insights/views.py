from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PlantLoss
from .serializers import PlantLossSerializer

class LossSummaryView(APIView):
    def get(self, request):
        queryset = PlantLoss.objects.all()
        serializer = PlantLossSerializer(queryset, many=True)
        return Response({'loss_summary': serializer.data})
