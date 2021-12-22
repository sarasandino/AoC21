# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 06:07:40 2021

@author: sarag
"""
data =open('input21.txt').read().split('\n')
data_spl=data[0].split(':')
pos_x=int(data_spl[1])
score_x=0
data_spl=data[1].split(':')
pos_y=int(data_spl[1])
score_y=0
i=1 #valor dado
c=0 #contador de lanzamientos
while True:
    c+=3
    pos_x=((pos_x)+(3*i+3))%10
    score_x+=pos_x
    if pos_x==0:
        score_x+=10
    if score_x>=1000:
        print('Solución:',score_y*c)
        break
    i+=3
    c+=3
    pos_y=((pos_y)+(3*i+3))%10
    score_y+=pos_y
    if pos_y==0:
        score_y+=10
    if score_y>=1000:
        print('Solución:',score_x*c)
        break
    i+=3

    