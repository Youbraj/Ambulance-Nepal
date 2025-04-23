from django import forms


class AmbulanceForm(forms.Form):
    # id = forms.IntegerField()
    name = forms.CharField(max_length=50,label='Name')
    contact = forms.CharField(max_length=25,label="Contact")
    address = forms.CharField(max_length=50,label="Address")

class UpdateData(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50,label='Name')
    contact = forms.CharField(max_length=25,label="Contact")
    address = forms.CharField(max_length=50,label="Address")

