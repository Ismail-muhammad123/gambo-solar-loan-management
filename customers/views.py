from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from customers.models import Customer
from loans.models import Loan, Payment, LoanItem



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "customers/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required(login_url="login")
def profile(request):
    try:
        customer_instance = get_object_or_404(Customer, user=request.user)
        loans = Loan.objects.filter(customer=customer_instance)
        return render(request, 'customers/profile.html', {'loans': loans})
    except Customer.DoesNotExist:
        logout(request)
        messages.error(request,"No Profile was found for this account")
        return render(request, "customers/login.html")

@login_required(login_url="login")
def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, customer=request.user.customer)
    loan_items = LoanItem.objects.filter(loan=loan)
    payments = Payment.objects.filter(loan=loan)
    return render(request, 'customers/loan_details.html', {'loan': loan, 'loan_items': loan_items, 'payments': payments})

