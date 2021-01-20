from django.contrib import admin
from .models import Product, Category, GetInTouch, Cart, ProductOrder, Checkout


class CheckoutAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(CheckoutAdmin, self).get_changeform_initial_data(request)
        get_data['user'] = request.user
        return get_data


admin.site.register(Checkout, CheckoutAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(GetInTouch)
admin.site.register(Cart)
admin.site.register(ProductOrder)