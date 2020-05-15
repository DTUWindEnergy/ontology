# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:00:33 2020

@author: mikf
"""

import yaml
import numpy as np
from py_wake.site import UniformSite, UniformWeibullSite
from py_wake.site.shear import PowerShear
import matplotlib.pyplot as plt

def read_yml(filename):
    with open(filename, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data

if __name__ == '__main__':
	# Uniform windspeed site
	data = read_yml('plant_energy_resource_mikf_uniform_resource_ws.yaml')
	p_wd = data['wind_resource']['uniform_resource']['probability']
	ti = data['wind_resource']['uniform_resource']['ti']
	ws = data['wind_resource']['uniform_resource']['wind_speed']
	h_ref = data['wind_resource']['uniform_resource']['shear']['h_ref']
	alpha = data['wind_resource']['uniform_resource']['shear']['alpha']
	site = UniformSite(p_wd=p_wd, ti=ti, ws=ws, shear=PowerShear(h_ref, alpha))
	plt.figure()
	site.plot_wd_distribution()

	# Uniform weibull site
	data = read_yml('plant_energy_resource_mikf_uniform_resource_weibull.yaml')
	p_wd = data['wind_resource']['uniform_resource']['probability']
	ti = data['wind_resource']['uniform_resource']['ti']
	a = data['wind_resource']['uniform_resource']['a']
	k = data['wind_resource']['uniform_resource']['k']
	site = UniformWeibullSite(p_wd=p_wd, a=a, k=k, ti=ti)
	plt.figure()
	site.plot_ws_distribution()

