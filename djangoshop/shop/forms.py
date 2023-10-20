from django import forms


class ProductForm(forms.Form):
    name_pr = forms.CharField(max_length=100)
    description_pr = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "The product's description"}))
    cost = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "The product's image"}))


class GetProductById(forms.Form):
    id_pr = forms.IntegerField()
