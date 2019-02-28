from taggit.forms import *
from django.forms import ModelForm
from .models import *

class TagModelForm(ModelForm):
    class Meta:
        model = Repository
        labels= {
            "repo_url": "Github Repository URL",
            "tags" : "Repo Tags:"
        }
        exclude = ()

class TagForm(forms.Form):
    tags = TagField()

    class Meta:
        labels = {
            "name" : "Repo Tags:"
        }
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'