from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Fundraiser, Pledge
from .serializers import FundraiserSerializer, PledgeSerializer

class FundraiserList(APIView):

   def get(self, request):
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

   def post(self, request):
        serializer = FundraiserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
          )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
          )

class FundraiserDetail(APIView):

   def get_object(self, pk):
      try:
         fundraiser = Fundraiser.objects.get(pk=pk)
         return fundraiser
      except Fundraiser.DoesNotExist:
         raise Http404
   def get(self, request, pk):
       fundraiser = self.get_object(pk)
       serializer = FundraiserDetailSerializer(fundraiser)

   def put(self, request, pk):
         fundraiser = self.get_object(pk)
         serializer = FundraiserDetailSerializer(
         instance=fundraiser,
         data=request.data,
         partial=True
      )
         if serializer.is_valid():
            serializer.save()
         return Response(serializer.data)

         return Response(
         serializer.errors,
         status=status.HTTP_400_BAD_REQUEST
      )
   