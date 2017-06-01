from __future__ import unicode_literals

from django.db import models

from django.contrib.gis.db import models


class Hurumaproject(models.Model):
	objectid_1 = models.IntegerField()
	objectid = models.IntegerField()
	entity = models.CharField(max_length=14)
	plotno_1 = models.CharField(max_length=20)
	fr_source1 = models.CharField(max_length=20)
	hact = models.FloatField()
	out = models.CharField(max_length=20)
	data = models.CharField(max_length=20)
	area = models.FloatField()
	perimeter = models.FloatField()
	acres = models.FloatField()
	hectares = models.FloatField()
	shape_leng = models.FloatField()
	no_offloor = models.IntegerField()
	type_dev = models.CharField(max_length=50)
	cracks_wl = models.CharField(max_length=50)
	verticalit = models.CharField(max_length=10)
	compliance = models.CharField(max_length=50)
	shape_le_1 = models.FloatField()
	shape_area = models.FloatField()
	geom = models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.plotno_1

# Auto-generated `LayerMapping` dictionary for Hurumaproject model
hurumaproject_mapping = {
	'objectid_1' : 'OBJECTID_1',
	'objectid' : 'OBJECTID',
	'entity' : 'ENTITY',
	'plotno_1' : 'PLOTNO_1',
	'fr_source1' : 'FR_SOURCE1',
	'hact' : 'HACT',
	'out' : 'OUT',
	'data' : 'DATA',
	'area' : 'AREA',
	'perimeter' : 'PERIMETER',
	'acres' : 'ACRES',
	'hectares' : 'HECTARES',
	'shape_leng' : 'Shape_Leng',
	'no_offloor' : 'No_offloor',
	'type_dev' : 'Type_dev',
	'cracks_wl' : 'Cracks_wl',
	'verticalit' : 'Verticalit',
	'compliance' : 'Compliance',
	'shape_le_1' : 'Shape_Le_1',
	'shape_area' : 'Shape_Area',
	'geom' : 'MULTIPOLYGON',
}



class Roysa(models.Model):
	entity = models.CharField(max_length=14)
	layer = models.CharField(max_length=32)
	level = models.FloatField()
	elevation = models.FloatField()
	plotno_1 = models.CharField(max_length=20)
	fr_source1 = models.CharField(max_length=20)
	data = models.CharField(max_length=20)
	name = models.CharField(max_length=254)
	type_of_de = models.CharField(max_length=50)
	cracks = models.CharField(max_length=50)
	plot_cover = models.IntegerField()
	verticalit = models.CharField(max_length=50)
	geom = models.MultiPolygonField(srid=32737)

	def __unicode__(self):
		return self.plotno_1

# Auto-generated `LayerMapping` dictionary for Roysa model
roysa_mapping = {
	'entity' : 'ENTITY',
	'layer' : 'LAYER',
	'level' : 'LEVEL',
	'elevation' : 'ELEVATION',
	'plotno_1' : 'PLOTNO_1',
	'fr_source1' : 'FR_SOURCE1',
	'data' : 'DATA',
	'name' : 'Name',
	'type_of_de' : 'Type_of_de',
	'cracks' : 'Cracks',
	'plot_cover' : 'Plot_Cover',
	'verticalit' : 'Verticalit',
	'geom' : 'MULTIPOLYGON',
}


class Viwandani(models.Model):
	building_d = models.CharField(max_length=254)
	building_1 = models.CharField(max_length=254)
	building_2 = models.IntegerField()
	building_3 = models.CharField(max_length=254)
	building_4 = models.CharField(max_length=254)
	building_5 = models.CharField(max_length=254)
	building_6 = models.IntegerField()
	building_7 = models.CharField(max_length=254)
	x = models.FloatField()
	y = models.FloatField()
	building_8 = models.FloatField()
	building_9 = models.FloatField()
	further_te = models.CharField(max_length=254)
	dev_type = models.CharField(max_length=254)
	dev_type_o = models.CharField(max_length=254)
	water_mete = models.IntegerField()
	defects_no = models.CharField(max_length=254)
	meta_insta = models.CharField(max_length=254)
	geom = models.MultiPointField(srid=4326)

	def __unicode__(self):
		return self.building_1

# Auto-generated `LayerMapping` dictionary for Viwandani model
viwandani_mapping = {
	'building_d' : 'building_d',
	'building_1' : 'building_1',
	'building_2' : 'building_2',
	'building_3' : 'building_3',
	'building_4' : 'building_4',
	'building_5' : 'building_5',
	'building_6' : 'building_6',
	'building_7' : 'building_7',
	'x' : 'x',
	'y' : 'y',
	'building_8' : 'building_8',
	'building_9' : 'building_9',
	'further_te' : 'further_te',
	'dev_type' : 'dev_type',
	'dev_type_o' : 'dev_type_o',
	'water_mete' : 'water_mete',
	'defects_no' : 'defects_no',
	'meta_insta' : 'meta_insta',
	'geom' : 'MULTIPOINT',
}

