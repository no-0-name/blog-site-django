from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'autocomplete': 'off',
                'class': 'form-control'
            })
    

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'autocomplete': 'off',
            'placeholder':'Comment here!',
            'rows':4,
            'cols':50
        }))
    
    class Meta:
        model = Comment
        fields = ['content']

