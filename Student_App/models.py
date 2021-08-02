from django.db import models

class Student(models.Model):
    """
        this model will contain student details like name,age,college_year,roll_no etc
    """
    name          = models.CharField(max_length=200,null=True)
    age           = models.IntegerField()
    year_choices  = (
        	( '1','First Year' ),
        	( '2','Second Year'),
        	( '3','Third Year' ),
        	( '4','Fourth Year'),
	    ) 
    college_year  = models.CharField(choices= year_choices, max_length=16)	
    roll_number   = models.CharField(max_length=10,null=True)
    created       = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    active        = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name.title()} | {self.roll_number.upper()} "
