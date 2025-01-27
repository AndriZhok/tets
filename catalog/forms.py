from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from catalog.models import Newspaper, Redactor, Topic


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = ["id", "title", "content", "topic", "publishers"]


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title",
            }
        )
    )


class RedactorForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["username", "first_name", "last_name", "email", "years_of_experience", "password"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(
        years_of_experience,
):
    if years_of_experience < 0 or years_of_experience > 100:
        raise ValidationError("Years of experience must be between 0 and 100")

    return years_of_experience


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username",
            }
        )
    )


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
            }
        )
    )
