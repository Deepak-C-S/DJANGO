from django import forms    

class studentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    place=forms.CharField()
    email=forms.EmailField()

    def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)<=3:
            raise forms.ValidationError("minimum no. of must be greater then 3 ! ")
        return n