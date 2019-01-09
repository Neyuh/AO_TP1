import anissa
import julie
import gauthier
import jeremy


## imports

import numpy as np
import itertools
from collections import namedtuple
import os
import random
from random import shuffle
from collections import namedtuple




if __name__ == '__main__':
    
    Combo = namedtuple('Combo', 'x solution')
    ### here's the main

    # nombre de points à l'initialisation
    n_init = 500
    ## nombre d'objectifs
    n_obj = 2
    ## nombre de voisins par voisinage
    n_neighbour = 30

    ## nombre de "chromosomes" permutés d'un voisin
    nPermut = 3

    # l'archive a été modifiée?
    archive_changed = False

    # nombre d'itérations
    iterations_count=0

    #n_max d'itérations sans changements
    limite = 10

    ## lecture de fichier
    filepath = 'Data/'
    dim, obj = read_data(filepath+'LAP-8-3objSOL.dat')
    ## initialisation de l'archive
    ini = init(dim, n_init)
    print(f"""
            dim : {dim} 
            obj : {obj}
            init : {init}
        """)


    obj = obj[0:n_obj]    
    
    ## obtention de tuples + cleanage archive
    tupled_ini = x_and_sol_to_named_tuple(ini,obj)
    archive = compare_and_delete(tupled_ini)
    
    i = 0 

    while (i<1000000) :

        #print('iteration #',i)

        ## select a random element from the archive
        original_neigh = random.choice(archive)
        #print(original_neigh)

        ## calcul de voisin d'un point de l'archive
        neighbourhood = findNeighboursA(original_neigh.x, n_neighbour,nPermut)

        ## calcul des solutions des voisins
        tupled_neighbourhood = x_and_sol_to_named_tuple(neighbourhood,obj)

        ## ajouter l'original au voisinage
        #tupled_neighbourhood.append(Combo(original_neigh.x,original_neigh.solution))
        tupled_neighbourhood.extend([original_neigh])

        ## Nettoyage du voisinage
        clean_neighbourhood = compare_and_delete(tupled_neighbourhood)

        ## ajouter les voisins à l'archive
        new_archive= add_and_update_archive(clean_neighbourhood,archive)

        ## comparer si l'ancien archive et la nouvelle sont identiques
        archive_changed = compare_old_and_new_archive(archive ,new_archive)

        ## nouvelle archive = l'ancienne
        archive = new_archive

        if (i%10000 == 0) :
            print('iteration #',i)
            print("LA nvlle archive : ", archive)

        ## condition d'arret
        iterations_count = update_iterations_count(archive_changed, iterations_count)
        test = stop_condition(iterations_count,limite)  

        i += 1

        if (i == 999999) :
            print('iteration #',i)
            print("LA nvlle archive : ", archive)

        if test == False:
            print("test", test , "iterations_count", iterations_count, "limite", limite)
            print("FINAL ARCHIVE : ", archive)
            break


    
    
