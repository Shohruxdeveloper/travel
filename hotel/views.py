from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Travel, Hotel, Klass
from .serializers import TravelSerializer, HotelSerializer, KlassSerializer



#----------------------------------------------------------------
# Travel Views

class TravelAPIView(APIView):
    def get(self, request: Request):
        travel = Travel.objects.all()
        return Response({"travel":TravelSerializer(travel, many=True).data})

    def post(self, request: Request):
        try:
            serializer = TravelSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            travel = serializer.save()
            return Response(TravelSerializer(travel).data)
        except:
            return Response({"message": "Travel does not exist"})


class TravelDetailAPIView(APIView):
    def get(self, request: Request, pk: int):
        try:
            travel = Travel.objects.get(pk=pk)
            return Response(TravelSerializer(travel).data)
        except:
            return Response({"message": "Travel does not exist"})

    def put(self, request: Request, pk: int):
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(instance=travel, data=request.data)
            serializer.is_valid(raise_exception=True)
            travel = serializer.save()
            return Response(TravelSerializer(travel).data)
        except:
            return Response({"message": "Travel does not exist"})

    def delete(self, request: Request, pk: int):
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({"message": "Travel deleted"})
        except:
            return Response({"message": "Travel does not exist"})


#----------------------------------------------------------------
# Hotel Views

class HotelAPIView(APIView):
    def get(self, request: Request):
        travel = Hotel.objects.all()
        return Response(travel.values())

    def post(self, request: Request):
        try:
            serializer = HotelSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            hotel = serializer.save()
            return Response(HotelSerializer(hotel).data)
        except:
            return Response({"message": "Hotel does not exist"})


class HotelDetailAPIView(APIView):
    def get(self, request: Request, pk: int):
        try:
            hotel = Hotel.objects.get(pk=pk)
            return Response(HotelSerializer(hotel).data)
        except:
            return Response({"message": "Hotel does not exist"})

    def put(self, request: Request, pk: int):
        try:
            hotel = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(instance=hotel, data=request.data)
            serializer.is_valid(raise_exception=True)
            hotel = serializer.save()
            return Response(HotelSerializer(hotel).data)
        except:
            return Response({"message": "Hotel does not exist"})

    def delete(self, request: Request, pk: int):
        try:
            hotel = Hotel.objects.get(pk=pk)
            hotel.delete()
            return Response({"message": "Hotel deleted"})
        except:
            return Response({"message": "Hotel does not exist"})


#----------------------------------------------------------------
# Klass Views

class KlassAPIView(APIView):
    def get(self, request: Request):
        klass = Klass.objects.all()
        return Response(klass.values())

    def post(self, request: Request):
        try:
            serializer = KlassSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            klass = serializer.save()
            return Response(KlassSerializer(klass).data)
        except:
            return Response({"message": "Klass does not exist"})


class KlassDetailAPIView(APIView):
    def get(self, request: Request, pk: int):
        try:
            klass = Klass.objects.get(pk=pk)
            return Response(TravelSerializer(klass).data)
        except:
            return Response({"message": "Klass does not exist"})

    def put(self, request: Request, pk: int):
        try:
            klass = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(instance=klass, data=request.data)
            serializer.is_valid(raise_exception=True)
            klass = serializer.save()
            return Response(TravelSerializer(klass).data)
        except:
            return Response({"message": "Klass does not exist"})


    def delete(self, request: Request, pk: int):
        try:
            klass = Klass.objects.get(pk=pk)
            klass.delete()
            return Response({"message": "Klass deleted"})
        except:
            return Response({"message": "Klass does not exist"})

