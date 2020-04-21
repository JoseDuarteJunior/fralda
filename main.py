#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------
# author      : Jose Antonio Duarte
# mail        : duarte936@gmail.com
# date        : 04.19.2020
# chama main.py imagem.jpg y-para ler n-para n ler exemplo
# python3 main.py 6.jpg y --var detectar e ler
# -----------------------------------------
import sys
import cv2
import backbone
from mrcnn import visualize
argumento = sys.argv[1]
if len(sys.argv) > 1:
    ativarleitura = sys.argv[2]
    ler = ativarleitura
image = cv2.imread(argumento)
backbone.predict(image,ler)


