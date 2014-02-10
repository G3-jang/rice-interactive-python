from django.db import models

loantype_choices = (('0','New'),
                    ('1','Used'),
                    ('2','Refinance'),)

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=100)
    #pub_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.question # + str(self.pub_date) (if u want two variables to display)

    

class Choice(models.Model):
    choice_text = models.CharField(max_length=25)
    poll = models.ForeignKey(Poll)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text

class Saletype(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class State(models.Model):
    state_name = models.CharField(max_length=25)
    state_abbr = models.CharField(max_length=5)
    def __unicode__(self):
        return self.state_name

class Person(models.Model):
    designation = models.CharField(max_length=5, default='Mr')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    saletype = models.ForeignKey(Saletype, null=True)
    loan_type = models.CharField(max_length=5, choices=loantype_choices, default='New')
    loan_amount = models.IntegerField(default=5000)
    credit_tier = models.PositiveIntegerField(default=700)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.ForeignKey(State, null=True)
    zipcode = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.firstname




    
