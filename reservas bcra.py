#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import pandas
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio


# In[17]:


colnames = [
            "año", "mes", "e.monetaria", "equivalencia", "u.monetaria or. con act.", "saldos", "promedio mensual"
            ]
dat = pandas.read_csv('reservas bcra.csv', names=colnames, sep=';', thousands=".")


# In[18]:


#Elimno primera fila
data = dat.drop(dat.index[0])


# In[19]:


día = []
tot = 0
while tot != 933:
    día.append(28)
    tot = tot+1
data.insert(2, "día", día)


# In[20]:


data["saldos"] = data["saldos"].str.replace(",","").astype(int)


# In[21]:


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


# In[22]:


df = data['día'].map(str) + '-' + data['mes'].map(str) + '-' + data['año'].map(str)


# In[23]:


df2 = pandas.concat([df, data], axis=1, sort=False)


# In[24]:


df2.head()


# In[25]:


pandas.to_datetime(df2[0])


# In[26]:


df2.rename(columns = {0:'fecha'}, inplace = True) 


# In[27]:


df2.tail()


# In[28]:


x=df2["fecha"]
y=df2["saldos"]

fig = px.line(df2, x, y,
              title='Reservas BCRA'
             )
fig.update_xaxes(
    rangeslider_visible=True,
)

fig.show()


# In[29]:


pio.write_html(fig, file='figure.html', auto_open=True)


# In[ ]:





# In[ ]:





# In[ ]:




