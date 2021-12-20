from cal.models import Event
from django import forms


class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    widgets = {
      'start_time': forms.DateInput(attrs={
        'type': 'datetime-local',
      },format='%Y-%m-%dT%H:%M'),
      'end_time': forms.DateInput(attrs={
        'type': 'datetime-local',
      }, format='%Y-%m-%dT%H:%M'),
    }
    exclude = []
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = '%Y-%m-%dT%H:%M'
    self.fields['end_time'].input_formats = '%Y-%m-%dT%H:%M'