from django.db import models

class Precinct(models.Model):
    pass

class Voter(models.Model):

    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    address = Models.CharField(max_length=100, null=True, blank=True)
    city = Models.CharField(max_length=100, null=True, blank=True)
    state = Models.CharField(max_length=100, null=True, blank=True)
    zipcode = Models.CharField(max_length=10, null=True, blank=True)

    precinct = Models.ForeignKey(Precinct, related_name='voter', null=True, blank=True)

    email = Models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(first_name, middle_name, last_name)