from django import forms
from .models import Review


class AddReview(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control"}),
            'rating': forms.Select(attrs={"class": "form-control"})
        }

    @staticmethod
    def get_instance(user, book):
        try:
            instance = user.review_set.get(book=book)
        except Review.DoesNotExist:
            instance = None
        return instance

    def populate(self):
        pass

