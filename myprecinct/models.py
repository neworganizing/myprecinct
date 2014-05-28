from django.db import models

class Precinct(models.Model):
    pass

class Voter(models.Model):

    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)

    precinct = models.ForeignKey(Precinct, related_name='voter', null=True, blank=True)

    email = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(first_name, middle_name, last_name)