# LIBRARIES

from owslib.wfs import WebFeatureService
from owslib.fes import *
from owslib.etree import etree
import pandas as pd
import csv, os

# Creating directories

os.makedirs('../../out', exist_ok = True)
os.makedirs('../../out/WFS_layers', exist_ok = True)

# Init

path = '../../out/WFS_layers/'

# WFS

wfs_belb = WebFeatureService(url = 'https://wfs.environnement.brussels/belb?', version = '1.1.0')
wfs_bm_equipment = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_equipment/wfs?service=wfs', version = '2.0.0')
wfs_bm_public_space = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_public_space/wfs?service=wfs', version = '2.0.0')
wfs_bm_urbis_topo = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_urbis_topo/wfs?service=wfs', version = '2.0.0')
wfs_bm_network = WebFeatureService(url = 'https://data.mobility.brussels/geoserver/bm_network/wfs?service=wfs', version = '1.1.0')
wfs_brugis = WebFeatureService(url = 'https://gis.urban.brussels/geoserver/ows?service=wfs', version = '2.0.0')
wfs_urbisAdm = WebFeatureService(url = 'http://geoservices-urbis.irisnet.be/geoserver/wms?', version = '1.1.0')

# Exporting the list of layers available

data = pd.DataFrame(list(wfs_belb.contents)); data.to_csv(path + 'wfs_belb.csv', index = False, header = False)
data = pd.DataFrame(list(wfs_bm_equipment.contents)); data.to_csv(path + 'wfs_bm_equipment.csv', index = False, header = False)
data = pd.DataFrame(list(wfs_bm_public_space.contents)); data.to_csv(path + 'wfs_bm_public_space.csv', index = False, header = False)
data = pd.DataFrame(list(wfs_bm_urbis_topo.contents)); data.to_csv(path + 'wfs_bm_urbis_topo.csv', index = False, header = False)
data = pd.DataFrame(list(wfs_bm_network.contents)); data.to_csv(path + 'wfs_bm_network.csv', index = False, header = False)
data = pd.DataFrame(list(wfs_brugis.contents)); data.to_csv(path + 'wfs_brugis.csv', index = False, header = False)
data = pd.DataFrame(list(wfs_urbisAdm.contents)); data.to_csv(path + 'wfs_urbis.csv', index = False, header = False)
