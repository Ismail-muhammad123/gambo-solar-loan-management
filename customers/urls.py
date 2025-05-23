from django.urls import path
from .views import profile, loan_detail, login_view, logout_view

urlpatterns = [
    path('', profile, name='customer_dashboard'),
    path('loan/<int:loan_id>/', loan_detail, name='loan_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
