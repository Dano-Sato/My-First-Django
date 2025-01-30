import re,bleach
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        # 제목에서 허용된 HTML 태그만 남기고 나머지 제거
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'a']
        title = bleach.clean(title, tags=allowed_tags, strip=True)

        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')

        # 내용에서 허용된 HTML 태그만 남기고 나머지 제거
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'a', 'p', 'ul', 'ol', 'li', 'blockquote']
        content = bleach.clean(content, tags=allowed_tags, strip=True)

        return content