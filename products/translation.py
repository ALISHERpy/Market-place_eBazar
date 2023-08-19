from .models import Product,Category
from modeltranslation.translator import TranslationOptions, register


@register(Product)
class NewsTranslationOptions(TranslationOptions):
    fields = ('category', 'title', 'description',  'address', )

@register(Category)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ("name",)