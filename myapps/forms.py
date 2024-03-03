from django import forms
from myapps.models import Books

# class BookForm(forms.Form):
#     book_name=forms.CharField()
#     author_name=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()



class BookModelForm(forms.ModelForm):
    
    class Meta:
        model=Books
        fields="__all__"

        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "pages":forms.NumberInput(attrs={"class":"form-control"})
        }