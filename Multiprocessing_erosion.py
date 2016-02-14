# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:33:10 2016

@author: admin
"""
##########
# Utilisation de la "Pool" pour remplacer l'utilisation d'une boucle for
# pour traiter X images contenues dans un dossier.
# L'objetif est de traiter 1 image par processus et d'optimiser le temps de
# traitement.
##########

from multiprocessing import Pool, Array, Process
import os
from mamba import *


 ############################## DONNEES ##############################
    # Liste les images contenues dans le dossier
path = 'C:\\Users\\admin\\Desktop\\Multiproc_Img\\'
os.chdir(path)
data = os.listdir(path)


 #####################################################################
 ############################## Definition de la fonction ############
def erosion(name):

    # Opening and creating images 
    im1 = imageMb(name)
    im2 = imageMb(im1)
    # Creating a reversed triangle (as opposed to the TRIANGLE found in Mamba 
    # source) structuring element
    reverse_triangle = structuringElement([0,1,6], grid=HEXAGONAL)
    # Performing an erosion of size 10 with the created structuring element
    erode(im1, im2, 10, se=reverse_triangle)
    im2.save(path+'erode_'+name)



 #####################################################################
 ############################## Definition des processus #############
if __name__ == '__main__':

    pool = Pool()                       # process per core
    pool.map(erosion, data)             # proces data_inputs iterable with pool
    
    
