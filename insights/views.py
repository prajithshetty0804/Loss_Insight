class WeeklyLossAPIView(APIView):
    def get(self, request):
        records = WeeklyLossRecord.objects.all()
        serializer = WeeklyLossSerializer(records, many=True)
        return Response({"weekly_loss_data": serializer.data})
