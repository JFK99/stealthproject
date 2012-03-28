from django.db import models

# Create your models here.

  
class idea(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.  
  
    VIEWED_CHOICES = (
    (u'Y', u'Viewed'),
    (u'N', u'Not Viewed'),
  
)
    description = models.TextField() #Like a TEXT field  
    viewed = models.CharField(max_length=1, choices=VIEWED_CHOICES)
    created = models.DateTimeField() #Like a DATETIME field  
  
    def __unicode__(self): #Tell it to return as a unicode string (The name of the description item) rather than just Object.  
        return self.description  