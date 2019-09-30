from django import forms
from firstapp.models import SiteUser,UserRole,Images
class SiteUserForm(forms.ModelForm):
    class Meta():
        model=SiteUser
        #fields = '__all__'
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "isActive"
                 ]

class UserRoleForm(forms.ModelForm):
    class Meta():
        model =UserRole
        # fields = '__all__'
        exclude = ["roleId",
                   "roleName",
                   "isActive"
                   ]

class ImagesForm(forms.ModelForm):
    class Meta():
        model=Images
        #fields = '__all__'
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userImage",
                 "userMobile",
                 "isActive"
                 ]