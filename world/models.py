from django.contrib.gis.db import models


class WorldBorder(models.Model):
    fips = models.CharField(max_length=2, null=True)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


from django.contrib.gis.db import models


class DpawRegion(models.Model):
    feat_id = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    ogc_fid = models.IntegerField(null=True, blank=True)
    office = models.CharField(max_length=64, null=True, blank=True)
    hectares = models.FloatField(null=True, blank=True)
    md5_rowhash = models.CharField(max_length=64, null=True, blank=True)

    geom = models.MultiPolygonField(srid=4283)

    def __str__(self):
        return self.region


