#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:58:13 2024

@author: shaique
"""
import numpy as np
data = dict()

fname = "/Users/shaique/Desktop/BioInf_IMP/BioInf_SS_2024/programming_course/project_pdfs/project_codes/91_sample_txt.txt"

with open(fname, 'rt') as ftext:
    lines = ftext.readlines()
    i = None
    j = None
    d = []
    f = []
    count = 0
    for line in lines:
        line = line.strip()
        if 'iIndex' in line:
            i = int(line.split(': ')[1].strip())
            d = []
            f = []
        if 'jIndex' in line:
            j = int(line.split(': ')[1].strip())
        if 'recorded-num-points' in line:
            n = int(line.split(': ')[1].strip())
        if line.startswith('#'):
            continue
        if line and not any(k in line for k in ('iIndex', 'jIndex', 'recorded-num-points')):
            data_line = line.split(' ')
            d.append(float(data_line[0]))
            f.append(float(data_line[1]))
            if count%2 == 0:
                s = 0
            if count%2 != 0:
                s = 1
            data[s, i, j] = (np.array(d), np.array(f))
            count += 1
            