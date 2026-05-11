from django import forms    

class studentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    place=forms.CharField()
    email=forms.EmailField()
    