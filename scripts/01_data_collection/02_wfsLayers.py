# LIBRARIES

from owslib.wfs import WebFeatureService
from owslib.fes import *
from owslib.etree import etree
import pandas as pd
import geopandas as gpd
import os

# Creating directories

os.makedirs('../../data', exist_ok = True)
os.makedirs('../../data/shp_layers', exist_ok = True)

# Init

path = '../../data/shp_layers/'

# WFS

wfs_belb = WebFeatureService(url = 'https://wfs.environnement.brussels/belb?', version = '1.1.0')
wfs_bm_equipment = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_equipment/wfs?service=wfs', version = '2.0.0')
wfs_bm_public_space = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_public_space/wfs?service=wfs', version = '2.0.0')
wfs_bm_urbis_topo = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_urbis_topo/wfs?service=wfs', version = '2.0.0')
wfs_bm_network = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_network/wfs?service=wfs', version = '1.1.0')
wfs_brugis = WebFeatureService(url = 'https://gis.urban.brussels/geoserver/ows?service=wfs', version = '2.0.0')
wfs_urbisAdm = WebFeatureService(url = 'http://geoservices-urbis.irisnet.be/geoserver/wms?', version = '1.1.0')

wfs_belb.timeout, wfs_bm_equipment.timeout, wfs_bm_public_space.timeout, wfs_bm_urbis_topo.timeout,
wfs_bm_network.timeout, wfs_brugis.timeout, wfs_urbisAdm.timeout = 120

# Exporting vector layers ------------------------------------------------------

# Brussels Environnement

layer = ('flood_hazardmap_2019_scale_1_10000', 'flood_hazardmap_fluvial_2019', 'flood_hazardmap_fluvial_extreme_depth', 'flood_hazardmap_fluvial_rp10_depth', 'flood_hazardmap_fluvial_rp100_depth',
  'inventaire_etat_sol_public', 'inventaire_sol_cadastre_ref', 'inventaire_sol_sensitivity_class',
  'map_bio_value_2000', 'map_bio_value_2020', 'map_bio_value_biotope', 'map_bio_value_ilots_18',
  'natura_2000_habitat', 'natura_2000_habitat_aqua', 'natura_2000_habitat_pt', 'natura_2000_station',
  'natural_reserve', 'protection_area_sonian_forest',
  'forest_path', 'greenway', 'public_green_area', 'reb_zone_centrale', 'reb_zone_developpement', 'reb_zone_liaison',
  'vegetation_2016', 'vegetation_2020', 'vegetation_2020_canopy',
  'water_polygon', 'water_river_open', 'water_river_cover',
  'vulnerable_zone', 'sensitive_area',
  'noise_air_lden_16', 'noise_air_ln_16', 'noise_multi_lden_16', 'noise_multi_ln_16', 'noise_rail_lden_16', 'noise_rail_ln_16', 'noise_road_lden_16', 'noise_road_ln_16') # list of layers to export

for l in layer: # extraction and export of each layer
    tmp = gpd.read_file(wfs_belb.getfeature(typename = 'BELB:' + l))
    tmp.to_file(path + 'BELB:' + l + '.shp')

# Urbis

    # Adm
layer = ('Bl', 'Bu', 'Cabu', 'Capa', 'Geo', 'Highways', 'Tu')

for l in layer:
    tmp = gpd.read_file(wfs_urbisAdm.getfeature(typename = 'UrbisAdm:' + l))
    tmp.to_file(path + 'UrbisAdm:' + l + '.shp')

    # Topo
tmp = gpd.read_file(wfs_bm_urbis_topo.getfeature(typename = 'bm_urbis_topo:street_light_point'))
tmp.to_file(path + 'bm_urbis_topo:street_light_point.shp')

# Brussels Mobility

    # Network
layer = ('ville30_detailed', 'Tunnelsections', 'Regional_roads', 'Zones_30', 'specialisation_velo', 'traffic_jam', 'urbis_sa_morphology')

for l in layer:
    tmp = gpd.read_file(wfs_bm_network.getfeature(typename = 'bm_network:' + l))
    tmp.to_file(path + 'bm_network:' + l + '.shp')

    # Equipment
tmp = gpd.read_file(wfs_bm_equipment.getfeature(typename = 'bm_equipment:noise_barrier_2006'))
tmp.to_file(path + 'bm_equipment:noise_barrier_2006' + '.shp')

    # Public space
tmp = gpd.read_file(wfs_bm_public_space.getfeature(typename = 'bm_public_space:trees'))
tmp.to_file(path + 'bm_public_space:trees.shp')

# BruGIS

tmp = gpd.read_file(wfs_brugis.getfeature(typename = 'URBAN_DPC_PN:Arbres_remarquables'))
tmp.to_file(path + 'URBAN_DPC_PN:Arbres_remarquables.shp')
