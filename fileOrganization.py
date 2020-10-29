# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:40:41 2020

@author: PEDRO
"""

import os
import pathlib
import shutil
from datetime import datetime

date = datetime.now();
dateString = date.strftime("%d_%m_%Y_%H_%M_%S");

path = pathlib.Path().absolute();
itensFiltrados = [];
listaArquivos = [];
listaDiretorios = [];
documentos = [];
i = 0;
j = 0;

musicasDestino = "MusicasOrganizadas_" + dateString;
docsDestino = "DocumentosOrganizados_" + dateString;

musicasExtensoes = ["mp3", "mp0", "m4a", "wav", "flac"];
docsExtensoes = [".docx", ".pdf", ".txt"];

listaDiretorios = os.listdir(path);

for a in listaDiretorios:
    if os.path.isfile(a) == True:
        listaArquivos.append(a);
        
pathDestinoDocs = os.path.join(path, docsDestino);
os.mkdir(pathDestinoDocs);

for arquivo in listaArquivos:
    for extensao in docsExtensoes:
        if arquivo.endswith(extensao) == True:
            shutil.move(os.path.join(path, arquivo), pathDestinoDocs);

pathDestinoMusicas = os.path.join(path, musicasDestino);
os.mkdir(pathDestinoMusicas);

for arquivo in listaArquivos:
    for extensao in musicasExtensoes:
        if arquivo.endswith(extensao) == True:
            shutil.move(os.path.join(path, arquivo), pathDestinoMusicas);

