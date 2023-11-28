from django.http import JsonResponse
from datetime import datetime
from transactions.models import Transactions, UnvalidTransactions
from transactions.serializers import TransactionSerializer, UnvalidTransactionSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UnvalidTransactionslist(APIView):
  def get(self, request):
    UnvalidTransactionList = UnvalidTransactions.objects.all()
    serializer = UnvalidTransactionSerializer(UnvalidTransactionList, many=True)
    return JsonResponse(serializer.data, safe=False)

  def post(self, request):
    data = request.data
    serializer = UnvalidTransactionSerializer(data=data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request):
    UnvalidTransactions.objecs.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ValidateTransaction(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request, pk):
    serializer = TransactionSerializer(data=UnvalidTransactions.objects.get(pk=pk).__dict__)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidTransactionList(APIView):
  def get(self, request, start_date, end_date):
    start_date = datetime.fromtimestamp(int(start_date))
    end_date = datetime.fromtimestamp(int(end_date))
    ValidateTransactionList = Transactions.objects.filter(created_date__gt=start_date, created_date__lt=end_date)
    #ValidateTransactionList = Transactions.objects.all()
    serializer = TransactionSerializer(ValidateTransactionList, many=True)
    return JsonResponse(serializer.data, safe=False)