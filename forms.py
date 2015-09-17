from django import forms
from .models import Product, Category

"""
ProductForm
Class that returns a form for products
"""
class ProductForm( forms.ModelForm ) :
    
    description = forms.CharField( widget = forms.Textarea )
    
    class Meta :
            
        model = Product
        fields = [ 'name', 'description', 'provider', 'sell_price', 'buy_price', 'category' ]
        
#End of ProductFrom Class

"""
CategoryForm
Class that returns a form for categories
"""
class CategoryForm( forms.ModelForm ) : 
    
    description = forms.CharField( widget = forms.Textarea )
    
    class Meta : 
        
        model = Category
        fields = [ 'name', 'description' ]
        
#End CategoryForm Class