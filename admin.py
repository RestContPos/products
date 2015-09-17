from django.contrib import admin
from .models import Product, Category
from .forms import ProductForm, CategoryForm

"""
ProductAdmin
This is the product presentation for the admin panel
"""
class ProductAdmin( admin.ModelAdmin ) :
    
    list_display = [ '__unicode__', "description", "timestamp", "provider", "updated" ]
    form = ProductForm
    
#End of Product Admin class

"""
CategoryAdmin
Thsi is the category presentation for the admin panel
"""
class CategoryAdmin( admin.ModelAdmin ) :
    
    list_display = [ '__unicode__', "description" ]
    form = CategoryForm
    
#End of category admin class

admin.site.register( Product, ProductAdmin )
admin.site.register( Category, CategoryAdmin )