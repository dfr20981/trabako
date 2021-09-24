#!/usr/bin/env python
# coding: utf-8

# In[ ]:


devuelveTexto = input("hola porfabor ingrese el un texto: ")

devuelveTexto = input("buelba a ingrese el texto: ")

print(f"{texto} {texto2}")


# In[ ]:


import json

from bson.son import RE_TYPE

qwe = input('texto1: ')
rty = input('texto2: ')
uio = input('texto3: ')
concatenaTodos = {}
concatenaTodos['arraid'].append({
't1': qwe,
't2': uio,
't3': uio,
})
json_format = json.dumps(concatenaTodos)
print (json_format)
print (type(json_format))


# In[ ]:


n1=float(input("Intro número uno: "))
n2=float(input("Intro numero dos: "))
division=n1/n2
if division <= 0:

print("error es menor o igual a cero: ",division)
else:
print("la division es mallor a cerro ",division)


# In[ ]:


n1=float(input("Intro número uno: "))
n2=float(input("Intro numero dos: "))
suma=n1+n2
if suma >= 100:

print("La suma es menor a 100: ",suma)
else:
print("La suma es menor a 100: ",suma)


# In[1]:


import numpy as np

matris = np.random.random((4,4))
matris


# In[ ]:




