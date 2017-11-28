
# coding: utf-8

# In[14]:

import plotly.plotly as py
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_csv(r'C:\Users\MKDesktop\Desktop\Work\plotlymaps2.csv')


# In[15]:

df.head(2)


# In[39]:

df['text'] = df['COUNTRY'] +'<br> Was: ' + df['GDP (BILLIONS)2010'].astype(str) + '<br> Is: '+ df['GDP (BILLIONS)2017'].astype(str) + '<br> Change: '+abs(df['GDP (BILLIONS)2017']-df['GDP (BILLIONS)2010']).astype(str) 
dfaff = df.loc[df['Continent'] == 'A']


data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['Percent Change from 2010 to 2017'],
        text = df['text'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            tickprefix = '',
            title = 'Change<br>From Before to After'),
      ) ]

layout = dict(
    title = 'Made up Data <br>Source:\
            <a href="www.urlgoeshere.com">\
            Fake Link</a>',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        projection = dict(
            type = 'orthographic'),
        domain = dict(
            x = [ 0, 1 ],
            y = [ 0, 1 ]
        ),
    ),        
    geo2 = dict(
        scope = 'africa',
        showframe = True,
        showcoastlines = True,
        showcountries = False,
        domain = dict(
            x = [ 0, 0.2 ],
            y = [ 0, 0.5 ]
        ),
        bgcolor = 'rgba(255, 255, 255, .75)',
    )
    )
inset = [
    go.Choropleth(
        locationmode = 'country names',
        locations = dfaff['COUNTRY'],
        z = df['Percent Change from 2010 to 2017'],
        text = df['Percent Change from 2010 to 2017'],
        colorscale = [[0,'rgb(0, 0, 0)'],[1,'rgb(0, 0, 0)']],
        autocolorscale = False,
        showscale = False,
        geo = 'geo2'
    ),
    go.Scattergeo(
        lon = [21.0936],
        lat = [7.1881],
        text = ['Africa<br>This is how you write on the map'],
        mode = 'text',
        showlegend = False,
        geo = 'geo2'
    )
]

fig = dict( data=data+inset, layout=layout )
#py.iplot( fig, validate=False, filename='d3-world-map' )

plot(fig, filename = r'C:\Users\MKDesktop\Desktop\Work\learning2.html', auto_open=False)


# In[22]:

df.head(2)
sortdf = df.sort_values(by=['GDP (BILLIONS)2017'])
sortdf = sortdf[sortdf['GDP (BILLIONS)2017'] > 100]  


# In[41]:

trace1 = go.Bar(
    x=sortdf['COUNTRY'],
    y=sortdf['GDP (BILLIONS)2010'],
    name='Rest of world',
    marker=dict(
        color='rgb(55, 83, 109)'
    )
)
trace2 = go.Bar(
    x=sortdf['COUNTRY'],
    y=sortdf['GDP (BILLIONS)2017'],
    name='China',
    marker=dict(
        color='rgb(26, 118, 255)'
    )
)
datab = [trace1, trace2]
layout = go.Layout(
    title='Globe Data Put into a Bar Chart',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='USD (millions)',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.3,
    bargroupgap=0.1
)

fig = go.Figure(data=datab, layout=layout)
plot(fig, filename = r'C:\Users\MKDesktop\Desktop\Work\learning2.html', fileopt='extend', auto_open=False)


# In[ ]:




# In[ ]:



