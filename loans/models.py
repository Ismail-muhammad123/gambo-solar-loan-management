import datetime
from django.db import models
from customers.models import Customer
from django.contrib.auth import get_user_model
from dateutil.relativedelta import relativedelta

User = get_user_model()


class Loan(models.Model):
    LOAD_STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("canceled", "Canceled")
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.PositiveIntegerField(default=12)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=LOAD_STATUS_CHOICES)

    def __str__(self):
        return self.customer.fullName + " - " + self.customer.email 

    @property
    def due_date(self):
        return self.created_at + relativedelta(months=self.period)

    @property
    def time_left(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        delta = self.due_date - now
        return delta.days // 30
    
    @property
    def total_paid(self):
        payments = self.payment_set.all()
        total = sum(payment.amount for payment in payments)
        percentage = (total / self.total_amount) * 100 if total > 0 else 0
        return f"{total} ({percentage}%) "

    @property
    def amount_left(self):
        total_paid = sum(payment.amount for payment in self.payment_set.all())
        return self.total_amount - total_paid

    # @property
    # def next_payment_status(self):
    #     now = datetime.datetime.now(datetime.timezone.utc)
    #     current_month = now.month
    #     current_year = now.year
    #     payments_this_month = self.payment_set.filter(
    #         payment_date__year=current_year, payment_date__month=current_month
    #     )
    #     if payments_this_month.exists():
    #         return "Paid for this month"
    #     else:
    #         return "Not paid for this month"
    

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


class LoanItem(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    @property
    def name(self):
        return self.product


    @property 
    def price(self):
        return self.product.price
    

    @property
    def amount(self):
        return self.product.price * self.quantity
    
