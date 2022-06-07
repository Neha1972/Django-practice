# Create your views here.
from rest_framework.views import APIView
from rest_framework.serializers import  CarItemsSerializer
from rest_framework.response import  Response


class CarItemViews(APIView):
    def post(self,request):
        serializer = CarItemsSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return  Response({"status":  "success", "data" : serialize.data})
        else:
            return Response({"status" : "Error", "data" : serialize.error})
