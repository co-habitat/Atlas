# LIBRARIES

from owslib.wfs import WebFeatureService
from owslib.fes import *
from owslib.etree import etree
import seaborn as sns
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import contextily as ctx
import fiona
import mapclassify
import folium
import csv
import os
from matplotlib.backends.backend_pdf import PdfPages

os.chdir('/Users/marlene.boura/Dropbox/CO-HABITAT_perso/Data Management/scripts')

# WFS

wfs_belb = WebFeatureService(url = 'https://wfs.environnement.brussels/belb?', version = '1.1.0')

wfs_belb.timeout = 120

# LOADING LAYERS

# Green ecological network
bioValue2020 = gpd.read_file(wfs_belb.getfeature(typename='BELB:map_bio_value_2020'))
bioValue2000 = gpd.read_file(wfs_belb.getfeature(typename='BELB:map_bio_value_2000'))

# MAPPING

fig, ax = plt.subplots(1, 1)

with PdfPages(r'../maps/EcologicalNetwork_green.pdf') as export_pdf:

    bioValue2020.plot(column = 'score', cmap = 'Greens_r', legend = True).set_axis_off()
    plt.title('Biological Score', fontsize = 14)
    bioValue2000.plot(column = 'eval', cmap = 'Greens_r', legend = True).set_axis_off()
    plt.title('Biological Score', fontsize = 14)
    export_pdf.savefig()
    plt.close()
