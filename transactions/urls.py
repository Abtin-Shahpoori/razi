from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from transactions.views import ValidateTransaction, UnvalidTransactionslist, ValidTransactionList

urlpatterns = [
    path('unvalid-transactions', UnvalidTransactionslist.as_view()),
    path('validate/<int:pk>', ValidateTransaction.as_view()),
    path('transactions/<str:start_date>/<str:end_date>', ValidTransactionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)