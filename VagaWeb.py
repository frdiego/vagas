

# -*- coding: utf-8 -*-
# Criado por: Diego Fernandes Rodrigues em 20181007
# Implementacao da busca por palavras chave no LinkedIn e Vagas.com.br
# Atualizado por: 
# Geting information from web page

## Importing the lib webbrowser
import webbrowser
import time

#List of key words for search
SearchKey = ['FEA','NVH','MEF','FEM','CFD','ANSYS','CFX','simulacao',
'fluidos','fluid','nastran','abaqus','Star-CCM','FEMAP','simulink',
'ncode','fadiga','calculista','elementos%20finitos','moldflow','HVAC',
'hypermesh','AVL','sap2000','CAE','PSD','modelica','dymola','ls-dyna']

#First half of the link URL
FirstHalf = ['https://www.linkedin.com/jobs/search/?f_TP=1%2C2&keywords=',
             'https://www.vagas.com.br/vagas-de-']

5#Second half of the link URL
SecondHalf = ['&location=Brazil&locationId=br%3A0&sortBy=DD',
              '?ordenar_por=mais_recentes']

for j in range(0,len(FirstHalf)):
    #for i in range(0,3):
    for i in range(0,len(SearchKey)):
        url = FirstHalf[j]+SearchKey[i]+SecondHalf[j]
        time.sleep(1)
        if j == 0:
            # Open URL in new browser window
            webbrowser.open_new(url) # opens in default browser
        else:
            # Open URL in a new tab
            webbrowser.open_new_tab(url) # opens in default browser
        
 #Other links
webbrowser.open_new_tab('https://semcon.com/join-us/jobs/')
 
webbrowser.open_new_tab('http://www.soditech.com.br/jobs.php')

webbrowser.open_new_tab('https://curriculos.esss.co/RM/Rhu-BancoTalentos/#/RM/Rhu-BancoTalentos/painelVagas/lista')