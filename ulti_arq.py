#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

caminho = r"C:\Users\SINAN\Downloads"
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

for arquivo in lista_arquivos:
    #descobrir a data do arquivo
    data = os.path.getmtime(f"{caminho}/{arquivo}")
    print(arquivo, data)


# In[ ]:





# In[ ]:




