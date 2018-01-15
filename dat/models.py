
try:
    from django.db import models
except:
    print('There was an error importing models from django.  Make sure you have django installed')
    quit()
    
# Define models below.


class Test(models.Model):
    name = models.TextField()
    
    