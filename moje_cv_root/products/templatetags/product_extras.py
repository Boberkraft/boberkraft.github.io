from django import template
import json
import os
from django.conf import settings
from django.utils import translation

register = template.Library()


def set_stack(self, x):
    self.stack = json.dumps(x)


@register.filter
def get_stack(self):
    return json.loads(self.stack)


@register.filter
def get_image(self):
    new = self.replace(os.path.join(
        settings.BASE_DIR,
        settings.STATICFILES_DIRS[0]),
        '')
    return new


@register.filter
def get_translation(text):
    languages = translation.get_language()
    start = text.find("=" + languages + '{')
    stack = 0
    end = None
    for i, letter in enumerate(text[start:]):
        if letter == '{':
            stack += 1
        if letter == "}":
            stack -= 1
            if stack == 0:
                end = start + i
                break

    if end is None:
        # raise ValueError("Mismatched tags" + str(text[start + 1:]))
        return text
    else:

        return text[start + len(languages) + 2:end]
