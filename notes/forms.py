from django import forms 
from django.core.exceptions import ValidationError
from .models import Notes 

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control my-5'}), #input ta3 title wla 3rid w ki tdirleh focus couleur ta3 outline yweli zreg fate7
            'text' : forms.Textarea(attrs={'class' : 'form-control mb-5'}) #kima lfog chawala textarea tji twila w 3rida kter
        }
        labels = {
            'text': 'write your thoughts here: '  #f la page fi blasset text bedelnaha b write your thoughts here
        }
    #def clean_title(self): 
        #title = self.cleaned_data['title']
        #if 'Django' not in title:
            #raise ValidationError('we only accept notes about django!')
        #return title
 #hadi function ki ndekhlo lel la page http://127.0.0.1:8000/smart/notes/new w ykon title contient kelmet Django yedina l lien http://127.0.0.1:8000/smart/notes wnsibo tema note li zednah m3a notes li dernahom mn 9bel
# kon title mandiroch fiha kelmet Django yaffichilna ghi flien li rana fih : we only accept notes about django