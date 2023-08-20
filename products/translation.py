from .models import Product,Category,Comment
from modeltranslation.translator import TranslationOptions, register


@register(Product)
class NewsTranslationOptions(TranslationOptions):
    fields = ('category', 'title', 'description',  'address', )

@register(Category)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ("name",)
    
@register(Comment)
class CommintTranslationOptions(TranslationOptions):
    fields = ('product',  'body', )
    