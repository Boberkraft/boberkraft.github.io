from django import template
import json

register = template.Library()


def set_stack(self, x):
    self.stack = json.dumps(x)


@register.filter
def get_stack(self):
    return json.loads(self.stack)