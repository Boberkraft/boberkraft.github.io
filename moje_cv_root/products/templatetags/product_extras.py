from django import template
import json
import os
from django.conf import settings

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