from transactions.models import Transactions, UnvalidTransactions
from rest_framework import serializers

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ['created_date', 'sender', 'amount']


class UnvalidTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnvalidTransactions
        fields = ['sender', 'amount']