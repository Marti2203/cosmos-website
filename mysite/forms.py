from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError, PasswordInput, CharField, HiddenInput
from .models.profile import Profile

#TODO Split into multiple files
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserRegistrationForm(ModelForm):
    password_repeat = CharField(
        label='Password Confirmation',
        max_length=128,
        widget=PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        # Set all fields to be mandatory
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password_repeat']
        # TODO follow
        # https://django.cowhite.com/blog/django-form-validation-and-customization-adding-your-own-validation-rules/
        widgets = {
            'password': PasswordInput(),
            'password_repeat': PasswordInput()
        }

    def clean(self):
        """
        Define checks. Throw `ValidationError` if form is invalid.
        """

        # Sets 'cleaned_data' attribute
        super(UserRegistrationForm, self).clean()

        # Check if user already exists
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise ValidationError(
                'There is already a user with this email in our system, please try with a different one.')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_repeat')
        # Validate password
        if not password1 == password2:
            raise ValidationError(
                'Your password and password confirmation do not match. Please make sure they are the same.')

    def save(self):
        """
        Override function to save. Required because form does not match `User` model
        (`User` model has no `password_repeat`)
        """
        username = email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        # TODO ask if make_password is required?
        password = self.cleaned_data.get('password')
        return User.objects.create_user(
            first_name=first_name, last_name=last_name,
            username=username, email=email, password=password,
        )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_nr',
            'gender', 'nationality',
            'department', 'program',
            'tue_id', 'card_number'
        ]

    def save(self, user_ref):
        self.instance.user = user_ref
        return super().save()


class ProfileUpdateForm(ProfileForm):
    class Meta:
        model = Profile
        fields = [
            'phone_nr',
            'gender', 'nationality',
            'department', 'program',
            'tue_id', 'card_number',
            'member_type', 'key_access'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['member_type'].disabled = True
        self.fields['key_access'].disabled = True
