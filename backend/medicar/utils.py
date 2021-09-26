from django.forms.fields import MultipleChoiceField
from django_filters.filters import Filter

SIGLA_ESTADOS = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE',
                 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
                 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
                 'SP', 'SE', 'TO',)


class MultipleValueField(MultipleChoiceField):
    def __init__(self, *args, field_class, **kwargs):
        self.inner_field = field_class()
        super().__init__(*args, **kwargs)

    def valid_value(self, value):
        return self.inner_field.validate(value)

    def clean(self, values):
        return values and [self.inner_field.clean(value) for value in values]


class MultipleValueFilter(Filter):
    field_class = MultipleValueField

    def __init__(self, *args, field_class, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, field_class=field_class, **kwargs)
