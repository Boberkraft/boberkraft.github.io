from django.db import models
import json
from django.conf import settings
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=300)
    image = models.FilePathField(path=settings.STATICFILES_DIRS[0], match='\w+\.(gif|png)$') # upload_to='uploads/%Y/%m/%d/'
    url = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    stack = models.CharField(blank=True, max_length=300)
    visible = models.BooleanField(default=True)


    def get_image(self, *args, **kwargs):
        print('XDDDD')
        return "23"

    def set_stack(self, x):
        self.stack = json.dumps(x)


    def get_stack(self):
        return json.loads(self.stack)
