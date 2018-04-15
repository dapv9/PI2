
from django.db import models
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.

class Frase(models.Model):


    texto = models.CharField(max_length=500)

    owner = models.ForeignKey('auth.User', related_name='frases', on_delete=models.CASCADE)
    highlighted = models.TextField()



def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the frase.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Serie, self).save(*args, **kwargs)
