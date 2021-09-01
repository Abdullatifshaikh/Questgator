from django.db import models

# Create your models here.
class DB_data(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=100)
    html_content=models.CharField(max_length=500000000000000000000000)

    @staticmethod
    def get_name(name):
        try:
            return DB_data.objects.get(name=name)
        except:
            return False

    def __str__(self):
        return self.name