# from django import forms
# from django.contrib.auth.models import User
# from .models import Profile

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     phone_number = forms.CharField(max_length=15)
#     permanent_address = forms.CharField(widget=forms.Textarea)
#     id_proof = forms.FileField(required=False)
#     profile_photo = forms.ImageField(required=False)
#     role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#             Profile.objects.create(
#                 user=user,
#                 phone_number=self.cleaned_data['phone_number'],
#                 permanent_address=self.cleaned_data['permanent_address'],
#                 id_proof=self.cleaned_data.get('id_proof', None),
#                 profile_photo=self.cleaned_data.get('profile_photo', None),
#                 role=self.cleaned_data['role']
#             )
#         return user
