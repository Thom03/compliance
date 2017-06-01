import os
from django.contrib.gis.utils import LayerMapping
from .models import Hurumaproject

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




huruma_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../portal/data/HurumaProject.shp'))

def run(verbose=True):
    lm = LayerMapping(Hurumaproject, huruma_shp, hurumaproject_mapping, transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)