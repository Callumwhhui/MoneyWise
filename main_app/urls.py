from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/accounts/', views.accounts, name='accounts'),
    path('accounts/<int:account_id>/', views.account_detail, name='account_detail'),
    path('budget/', views.budget, name='budget'),
    path('stocks/', views.stocks, name='stocks'),
    path('calculator/', views.calculator, name='calculator'),
    path('taxes/', views.taxes, name='taxes'),
    path('accounts/signup/', views.signup, name='signup'),
    path('transactions/', views.transactions, name='transactions'),
    path('transactions/incomes', views.incomes, name='incomes'),
    path('transactions/expenses', views.expenses, name='expenses'),
    path('demo_account/', views.demo_account, name='demo_account'),
    path('accounts/create/', views.AccountCreate.as_view(), name='account_create'),
    path('accounts/<int:pk>/update/', views.AccountUpdate.as_view(), name='account_update'),
    path('accounts/<int:pk>/delete/', views.AccountDelete.as_view(), name='account_delete'),
    path('transactions/incomes/create/', views.IncomeCreate.as_view(), name='income_create'),
    path('transactions/incomes/<int:pk>/update/', views.IncomeUpdate.as_view(), name='income_update'),
    path('transactions/incomes/<int:pk>/delete/', views.IncomeDelete.as_view(), name='income_delete'),
    path('transactions/expenses/create/', views.ExpenseCreate.as_view(), name='expense_create'),
    path('transactions/expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expense_update'),
    path('transactions/expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense_delete'),
    path('budget/create/', views.BudgetCreate.as_view(), name='budget_create'),
    path('budget/<int:pk>/update/', views.BudgetUpdate.as_view(), name='budget_update'),
    path('budget/<int:pk>/delete/', views.BudgetDelete.as_view(), name='budget_delete'),
]