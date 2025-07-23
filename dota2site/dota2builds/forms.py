from django import forms

from dota2builds.models import Build, BuildItemInfo
from dota2site import settings


class BuildForm(forms.ModelForm):
    template_name = "forms/build-account-base.html"

    delete = forms.BooleanField(label="Удалить", required=False)

    class Meta:
        model = Build
        fields = ('name', 'hero')


class FilterBuildsForm(forms.Form):
    hero = forms.CharField(max_length=30, required=False, label="Имя героя")
    heroslug = forms.CharField(max_length=30, required=False, label="Тех. имя героя")
    heroid = forms.IntegerField(min_value=0, initial=0, required=False, label="ID героя")
    name = forms.CharField(max_length=30, required=False, label="Имя сборки")
    owner = forms.CharField(max_length=30, required=False, label="Имя создателя")
    ownerid = forms.IntegerField(min_value=0, initial=0, required=False, label="ID создателя")
    offset = forms.IntegerField(min_value=0, initial=0, required=False, label="Сдвиг")
    count = forms.IntegerField(min_value=0, max_value=100, initial=settings.DEFAULT_COUNT_BUILDS_IN_ONE_QUERY, required=False, label="Количество записей")

    __fvalues = (
        ("name", "name__istartswith"),
        ("hero", "hero__name__istartswith"),
        ("heroslug", "hero__slug__istartswith"),
        ("heroid", "hero__pk"),
        ("owner", "owner__username__istartswith"),
        ("ownerid", "owner__pk"),
    )

    def filter(self, queryset):
        for clean_key, filter_key in FilterBuildsForm.__fvalues:
            if value := self.cleaned_data.get(clean_key):
                queryset = queryset.filter(**{filter_key: value})

        offset = self.cleaned_data.get("offset") or 0
        count = self.cleaned_data.get("count") or settings.DEFAULT_COUNT_BUILDS_IN_ONE_QUERY

        return queryset[offset:offset+count]


class CustomBuildItemInfoFormSet(forms.BaseInlineFormSet):
    ordering_widget = forms.HiddenInput()


BuildItemOrderFormSet = forms.inlineformset_factory(
    Build,
    BuildItemInfo,
    fields=('item', 'description'),
    formset=CustomBuildItemInfoFormSet,
    extra=0,
    can_order=True,
    can_delete=True
)
