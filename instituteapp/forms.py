from django import forms
from multiselectfield import MultiSelectFormField

class FeedBackForm(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Ratting",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Ratting'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number'
            }
        )
    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'Rest API')
    )
    courses = MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('mrg', 'Morning'),
        ('aftn', 'Afternoon'),
        ('eveng', 'Evening'),
        ('night', 'Night')

    )
    shift = MultiSelectFormField(max_length=200, choices=SHIFTS_CHOICES)

    LOCATIONS_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Banglore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    locations = MultiSelectFormField(max_length=200, choices=LOCATIONS_CHOICES)

    GENDER_CHOICES = (
        ('m',"male"),
        ('f',"Female")
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICES
    )
    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )