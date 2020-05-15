# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:00:33 2020

@author: mikf
"""

import yaml
import numpy as np


def read_yml(filename):
    with open(filename, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data

if __name__ == '__main__':
#    data = read_yml('plant_energy_turbine.yaml')
    data = read_yml('plant_energy_resource_mikf.yaml')
#    data = read_yml("C:\Sandbox\Git\PyWake\py_wake\examples\data\iea37\iea37-windrose.yaml")
