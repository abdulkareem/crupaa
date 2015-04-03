from django.contrib import admin
from sito.models import *

from image_cropping import ImageCroppingMixin

# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Page, MyModelAdmin)
admin.site.register(Aziende, MyModelAdmin)
admin.site.register(Categorie, MyModelAdmin)
admin.site.register(Prodotti, MyModelAdmin)
admin.site.register(Immagini, MyModelAdmin)
admin.site.register(Slider, MyModelAdmin)