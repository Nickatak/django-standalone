import os
import django
# Hackish, I know, but these must come before you try to import models.  Not PEP8 compliant.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from dat.models import *


#Define any functions below.  These can be called right here in the script, but I'd prefer that they were imported and called elsewhere and limited with __all__. See: test.py
def t_add():
    Test.objects.create(name='asdf')
    
    
def get_all():
    all = Test.objects.all()
    
    for obj in all:
        print(obj.name)
        
def clean():
    Test.objects.all().delete()
        
        
        



