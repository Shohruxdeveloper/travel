from django.db import models





class Klass(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars_number = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    term = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    klass = models.ForeignKey(Klass, null=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,  null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name