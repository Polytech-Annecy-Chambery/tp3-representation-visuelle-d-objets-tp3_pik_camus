# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:46:35 2021

@author: Théo
"""
import pygame


pygame.init()
ecran = pygame.display.set_mode((300, 200)) # definition de la fenêtre.

continuer = True
while continuer:
    for event in pygame.event.get(): # boucle qui attend qu'on événement quelconque se produise
        if event.type == pygame.KEYDOWN: 
            continuer = False  # si un événement se présente alors le programme se ferme.

pygame.quit()
