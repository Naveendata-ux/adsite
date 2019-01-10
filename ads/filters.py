from .models import Ad
from django import forms
import django_filters


CATEGORY_CHOICES = (
    ('electronics', 'Electronics'),
    ('software', 'Software'),
    ('home', 'Home'),
    ('clothes', 'Clothes'),
    ('tools', 'Tools'),
    ('camping', 'Camping')
)


class AdFilter(django_filters.FilterSet):
    category = django_filters.MultipleChoiceFilter(choices=CATEGORY_CHOICES,
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='<b>CATEGORY</b>')
    price__lt = django_filters.NumberFilter(name='price',
                                            lookup_expr='lt',
                                            label='to')
    price__gte = django_filters.NumberFilter(name='price',
                                             lookup_expr='gte',
                                             label='<b>PRICE</b>')

    class Meta:
        model = Ad
        fields = ['category', 'price__gte', 'price__lt', ]
