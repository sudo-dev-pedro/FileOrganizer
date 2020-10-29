# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:40:41 2020

@author: PEDRO
"""

import os
import pathlib
import shutil
from datetime import datetime

#Coleta da data atual
date = datetime.now();
#Conversão da data para string e realizando a formatação
dateString = date.strftime("%d_%m_%Y_%H_%M_%S");

# Coletando o path absoluto atual
path = pathlib.Path().absolute();
# Inicializando as váriaveis e listas
itensFiltrados = [];
listaArquivos = [];
listaDiretorios = [];
documentos = [];
i = 0;
j = 0;

# Nome das pastas de destino
musicasDestino = "MusicasOrganizadas_" + dateString;
docsDestino = "DocumentosOrganizados_" + dateString;

# Extensões que serão averiguadas
musicasExtensoes = ["mp3", "mp0", "m4a", "wav", "flac"];
docsExtensoes = [".docx", ".pdf", ".txt"];

# Lista de diretorios do path atual
listaDiretorios = os.listdir(path);

# Coleta todos os arquivos do diretório
for a in listaDiretorios:
    if os.path.isfile(a) == True:
        listaArquivos.append(a);
        
pathDestinoDocs = os.path.join(path, docsDestino);
# Criação do diretório para os documentos
os.mkdir(pathDestinoDocs);

for arquivo in listaArquivos:
    for extensao in docsExtensoes:
        if arquivo.endswith(extensao) == True:
            shutil.move(os.path.join(path, arquivo), pathDestinoDocs);

pathDestinoMusicas = os.path.join(path, musicasDestino);
# Criação do diretório para os documentos
os.mkdir(pathDestinoMusicas);

for arquivo in listaArquivos:
    for extensao in musicasExtensoes:
        if arquivo.endswith(extensao) == True:
            shutil.move(os.path.join(path, arquivo), pathDestinoMusicas);

