# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:05:57 2016

@author: yixuantan
"""

n = 200 # number of colors to map
max_value = 16581375 #255**3
interval = int(max_value / n)
colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
res = [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]
f = open('colormap.xml', 'w')
f.write("<ColorMap name=\"GrainOrientation\" space=\"RGB\">\n")
for i in range(200):
    index = i + 1;
    f.write("<Point x=\"" + str(index) + "\" o=\"1\" r=\"" + str(res[i][0]*1.0/255) + "\" g=\"" + str(res[i][1]*1.0/255) + "\" b=\"" + str(res[i][2]*1.0/255) + "\"/>\n")
f.write("</ColorMap>\n")
f.close()
