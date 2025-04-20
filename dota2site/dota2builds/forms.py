from django import forms

from dota2builds.models import Item, Build, BuildItemOrder

BuildItemOrderFormSet = forms.inlineformset_factory(
    Build,
    BuildItemOrder,
    fields=('item', 'order'),
    extra=1,
    can_delete=True
)

class BuildForm(forms.ModelForm):
    template_name = "forms/build_form.html"

    class Meta:
        model = Build
        fields = ('name', 'hero')
