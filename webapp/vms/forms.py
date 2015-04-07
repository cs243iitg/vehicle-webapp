from vms import models
from django.contrib.auth.models import User
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget

class TheftForm(forms.ModelForm):
    """
    User form for reporting theft
    """

    class Meta:
        model = models.TheftReport
        exclude = ('reporter',)
        widgets = {
            'theft_time': DateTimeWidget(usel10n = True, bootstrap_version=3),
            'remarks': forms.Textarea(attrs={'rows':6}),
        }

    def __init__(self, *args, **kwargs):
        super(TheftForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })
