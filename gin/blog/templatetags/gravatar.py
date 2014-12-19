from django import template
import hashlib

register = template.Library()

@register.filter
def gravatar(value):
  return hashlib.md5(value).hexdigest()
