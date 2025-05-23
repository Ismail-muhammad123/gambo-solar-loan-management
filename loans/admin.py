from django.contrib import admin
from .models import Loan, Payment, LoanItem, Product


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1

class LoanItemsInline(admin.TabularInline):
    model = LoanItem
    extra = 1

class LoanAdmin(admin.ModelAdmin):

    inlines = [PaymentInline, LoanItemsInline]


class LoanItemAdmin(admin.ModelAdmin):
    list_display = [
        "loan",
        "product",
        "quantity",
        "created_at"
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "created_at",
    ]

    order_by = ["price", "created_at"]


class PaymentAdmin(admin.ModelAdmin):
    list_display=[
        "amount",
        "loan",
        "payment_date",
        "recorded_by",
    ]

admin.site.register(Loan, LoanAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(LoanItem, LoanItemAdmin)
admin.site.register(Product, ProductAdmin)



admin.site.site_header = "Gambo Solar Loan Administration"
admin.site.site_title = "Gambo Solar Admin Portal"
admin.site.index_title = "Welcome to Gambo Solar Loan Management"