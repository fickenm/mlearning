
# coding: utf-8

# In[1]:

from pyorbital import astronomy
from datetime import datetime
import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go

days31 = [1, 3, 5, 7, 8, 10, 12]
days28 = [2]
days30 = [4, 6, 9, 11]
hours = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

year = 2017
month = 5
day = 15

#utc_time = datetime(year, month, day, 15, 45)
lon = 12
lat = 80
#astronomy.sun_zenith_angle(utc_time, lon, lat)


# In[2]:

lat10 = 10
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat10))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat10))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat10))

chunks10 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat20 = 20
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat20))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat20))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat20))

chunks20 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat30 = 30
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat30))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat30))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat30))

chunks30 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat40 = 40
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat40))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat40))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat40))

chunks40 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat50 = 50
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat50))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat50))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat50))

chunks50 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat60 = 60
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat60))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat60))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat60))

chunks60 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat70 = 70
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat70))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat70))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat70))

chunks70 = [angles[x:x+24] for x in range(0, len(angles), 24)]

lat80 = 80
angles = []
for m in range(1,13):
    if m in days31:
        for d in range(1,32):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat80))
    if m in days28:
        for d in range(1,29):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat80))
    if m in days30:
        for d in range(1,31):
            for h in range(0, 24):
                utc_time = datetime(year, m, d, h, 45)
                angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat80))

chunks80 = [angles[x:x+24] for x in range(0, len(angles), 24)]


# lat2 = 50
# angles = []
# for m in range(1,13):
#     if m in days31:
#         for d in range(1,32):
#             for h in range(0, 24):
#                 utc_time = datetime(year, m, d, h, 45)
#                 angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat2))
#     if m in days28:
#         for d in range(1,29):
#             for h in range(0, 24):
#                 utc_time = datetime(year, m, d, h, 45)
#                 angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat2))
#     if m in days30:
#         for d in range(1,31):
#             for h in range(0, 24):
#                 utc_time = datetime(year, m, d, h, 45)
#                 angles.append(astronomy.sun_zenith_angle(utc_time, lon, lat2))
# 
# chunks2 = [angles[x:x+24] for x in range(0, len(angles), 24)]
# len(angles)
# len(chunks2)

# In[12]:

latbins = [0, 10, 20, 30, 40, 50, 60, 70, 80]

num_lists = len(latbins)
latlists = []
for p in range(num_lists):
    latlists.append([])
latlists

for i, j in enumerate(latbins):
    if j == 40:
        latlists[i].append(i)


# angles = []
# for bin in latbins:
#     for m in range(1,13):
#         if m in days31:
#             for d in range(1,32):
#                 for h in range(0, 24):
#                     utc_time = datetime(year, m, d, h, 45)
#                     angles.append(astronomy.sun_zenith_angle(utc_time, lon, bin))
#         if m in days28:
#             for d in range(1,29):
#                 for h in range(0, 24):
#                     utc_time = datetime(year, m, d, h, 45)
#                     angles.append(astronomy.sun_zenith_angle(utc_time, lon, bin))
#         if m in days30:
#             for d in range(1,31):
#                 for h in range(0, 24):
#                     utc_time = datetime(year, m, d, h, 45)
#                     angles.append(astronomy.sun_zenith_angle(utc_time, lon, bin))
# 
# chunks7 = [angles[x:x+24] for x in range(0, len(angles), 24)]
# len(angles)
# len(chunks7)

# In[3]:

import plotly.plotly as py
import plotly.graph_objs as go
x = []
y = []
x.extend(range(1, 366))
y.extend(range(0, 24))

data1 = go.Contour(
        z=chunks10,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data2 = go.Contour(
        z=chunks20,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data3 = go.Contour(
        z=chunks30,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data4 = go.Contour(
        z=chunks40,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data5 = go.Contour(
        z=chunks50,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data6 = go.Contour(
        z=chunks60,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data7 = go.Contour(
        z=chunks70,
        x=x,
        y=y,
        colorscale='RdBu'
    )
data8 = go.Contour(
        z=chunks80,
        x=x,
        y=y,
        colorscale='RdBu'
    )

data = [data1, data2, data3, data4, data5, data6, data7, data8]

updatemenus=list([
    dict(type = 'buttons',
         active = -1,
        buttons = list([   
            dict(label = '10',
                 method = 'update',
                 args = [{'visible': [True, False, False, False, False, False, False, False]},
                         {'title': '10 Degrees'}]),
            dict(label = '20',
                 method = 'update',
                 args = [{'visible': [False, True, False, False, False, False, False, False]},
                         {'title': '20 Degrees'}]),
            dict(label = '30',
                 method = 'update',
                 args = [{'visible': [False, False, True, False, False, False, False, False]},
                         {'title': '30 Degrees'}]),
            dict(label = '40',
                 method = 'update',
                 args = [{'visible': [False, False, False, True, False, False, False, False]},
                         {'title': '40 Degrees'}]),
            dict(label = '50',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True, False, False, False]},
                         {'title': '50 Degrees'}]),
            dict(label = '60',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, True, False, False]},
                         {'title': '60 Degrees'}]),    
            dict(label = '70',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, True, False]},
                         {'title': '70 Degrees'}]),
            dict(label = '80',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, True]},
                         {'title': '80 Degrees'}]),   
         ]),
    )
])
layout = dict(title='Sun Elevation Angle plots', showlegend=False,
              updatemenus=updatemenus)

fig = dict(data=data, layout=layout)
plot(fig, filename = r'C:\Users\MKDesktop\Desktop\Work\learning.html', auto_open=False)


# updatemenus=list([
#     dict(
#         buttons=list([   
#             dict(
#                 args=['type', 'contour'],
#                 label='Contour Plot',
#                 method='restyle'
#             ),
#             dict(
#                 args=['type', 'heatmap'],
#                 label='Heatmap',
#                 method='restyle'
#             ),    
#             dict(
#                 args=['type', 'surface'],
#                 label='Surface',
#                 method='restyle',
# 
#             ),    
#             dict(
#                 args=['data2', 'data2'],
#                 label='Data2',
#                 method='update'
#             )   
#         ]),
#         direction = 'down',
#         pad = {'r': 10, 't': 10},
#         showactive = True,
#         x = 0.1,
#         xanchor = 'left',
#         y = 1.1,
#         yanchor = 'top' 
#     ),
# ])

# In[ ]:




# In[ ]:




# In[4]:

chunks10


# In[6]:

len(chunks10[0])


# In[7]:

chunks10[0]


# In[ ]:



