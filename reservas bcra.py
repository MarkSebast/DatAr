#!/usr/bin/env python
# coding: utf-8

# In[155]:


import matplotlib.pyplot as plt
import pandas
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio


# In[2]:


colnames = [
            "año", "mes", "e.monetaria", "equivalencia", "u.monetaria or. con act.", "saldos", "promedio mensual"
            ]
dat = pandas.read_csv('reservas bcra.csv', names=colnames, sep=';', thousands=".")


# In[3]:


#Elimno primera fila
data = dat.drop(dat.index[0])


# In[4]:


día = []
tot = 0
while tot != 933:
    día.append(28)
    tot = tot+1
data.insert(2, "día", día)


# In[5]:


data["saldos"] = data["saldos"].str.replace(",","").astype(int)


# In[6]:


#Convirtiendo meses
data.loc[data['mes'] == 'enero', 'mes'] = 1
data.loc[data['mes'] == 'enero ', 'mes'] = 1
data.loc[data['mes'] == 'febrero', 'mes'] = 2
data.loc[data['mes'] == 'marzo', 'mes'] = 3
data.loc[data['mes'] == 'abril', 'mes'] = 4
data.loc[data['mes'] == 'mayo', 'mes'] = 5
data.loc[data['mes'] == 'junio', 'mes'] = 6
data.loc[data['mes'] == 'julio', 'mes'] = 7
data.loc[data['mes'] == 'agosto', 'mes'] = 8
data.loc[data['mes'] == 'septiembre', 'mes'] = 9
data.loc[data['mes'] == 'octubre', 'mes'] = 10
data.loc[data['mes'] == 'noviembre', 'mes'] = 11
data.loc[data['mes'] == 'diciembre', 'mes'] = 12


# In[7]:


df = data['día'].map(str) + '-' + data['mes'].map(str) + '-' + data['año'].map(str)


# In[8]:


df2 = pandas.concat([df, data], axis=1, sort=False)


# In[9]:


df2.head()


# In[10]:


pandas.to_datetime(df2[0])


# In[11]:


df2.rename(columns = {0:'date'}, inplace = True) 


# In[14]:


df2['date'] = pandas.to_datetime(df2['date'])
df2.date.dt.strftime('%Y%-m%-d')


# In[15]:


df2.tail()


# In[150]:


fig = go.Figure()

fig.add_trace(
   go.Scatter(x=list(df2.date), 
              y=list(df2.saldos), 
              name="reservas",
                line=dict(color='green', width=1),
                marker={"size": 3},
                mode="lines+markers",
                showlegend=False,
                 )
)




#Título
fig.update_layout(
    title_text="Reservas brutas BCRA por mes"
)



#RangeSlider and selector
fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="todate"),
            dict(count=10, label="10y", step="year", stepmode="todate"),
        ])),
    
    rangeslider=dict(visible=True,
                    range=["1940-01-28", "2020-08-28"])
)

fig.update_xaxes(range=["1940-01-28", "2020-08-28"])
     

#Color range selector
fig.update_xaxes(rangeselector_bgcolor='gray')


#Color de fondo
fig.update_layout(
    dragmode="pan",
    hovermode="x",
    legend=dict(traceorder="reversed"),
    height=700,
    template="plotly_dark",
    margin=dict(
        t=100,
        b=100
    )
)

    
#


fig.show()

#When using "all" button, range changes to dates out of the df. Can't find a solution to that


# In[156]:


pio.write_html(fig, file='reservas bcra.html', auto_open=True)

