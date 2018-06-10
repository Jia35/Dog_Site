from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=15)
    residential_location = forms.CharField(max_length=30)
    housing_condition = forms.CharField(max_length=100)
    equipment = forms.CharField(max_length=100)


'''    
    account = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to = 'user_pictures')
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    residential_location = models.CharField(max_length=30)
    housing_condition = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=3,decimal_places=1)
    evaluation = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default = timezone.now)
'''
