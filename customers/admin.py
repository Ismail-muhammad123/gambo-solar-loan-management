from django.contrib import admin
from .models import Customer, Guarantor



@admin.register(Guarantor)
class GuarantorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "address",
        "relationship",
        "customer",
    ]

class GuarantorInline(admin.TabularInline):
    model = Guarantor
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "phoneNumber",
        "email",
        "address",
        "date_date",
        "passport_photo",
    ]

    search_fields = ["phoneNumber", "email", "nin", "bvn"]
    list_filter = ["address"]
    ordering = ["date_date"]

    inlines = [GuarantorInline]