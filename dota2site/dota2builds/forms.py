from django import forms

from dota2builds.models import Build, BuildItemInfo


class BuildForm(forms.ModelForm):
    template_name = "forms/build-form.html"

    delete = forms.BooleanField(label="Удалить", required=False)

    class Meta:
        model = Build
        fields = ('name', 'hero')


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
