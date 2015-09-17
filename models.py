from django.db import models
from providers.models import Provider

"""
Category model
"""
class Category( models.Model ) :

    name = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 1000, default = '' )
    
    def __unicode__( self ) :
        return self.name

#End of Category Model

"""
Product model
"""
class Product( models.Model ) :
    
    name = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 1000, default='' )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    provider = models.ForeignKey( Provider, default=1 )
    category = models.ForeignKey( Category, default=1 )
    
    sell_price = models.DecimalField( max_digits=19, decimal_places=2, default=0.0 )
    buy_price = models.DecimalField( max_digits=19, decimal_places=2, default=0.0 )
    
    def __unicode__( self ) :
	    return self.name

#End of Company model