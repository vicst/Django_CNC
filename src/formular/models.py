from django.db import models

# Create your models here.
class form(models.Model):
    data_centralizarii      = models.DateField()
    nr_uaturi_cad_fin       = models.SmallIntegerField()
    nr_sectoare_cad_fin     = models.SmallIntegerField()
    sup_carti_fun           = models.DecimalField(max_digits = 11, decimal_places= 4)
    nr_uaturi_in_lucru      = models.SmallIntegerField()
    nr_sc_in_lucru          = models.SmallIntegerField()
    nr_contracte_finantare  = models.SmallIntegerField()
    nr_contracte_servicii   = models.SmallIntegerField()
    timestamp               = models.DateTimeField(auto_now_add = True)
    updated                 = models.DateTimeField(auto_now = True)
    def __str__(self):
        return str(self.data_centralizarii)