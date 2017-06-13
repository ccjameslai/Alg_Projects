# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:33:35 2017

@author: 2017041801
"""

import math

import numpy as np

import simulationdata as simdata

def Euclidean_similarity(target, comp_one):
    common_ranked_items = [itm for key in target.values() for itm in key.keys() \
                           if itm in simdata.data[comp_one].keys()]
    
    target_rated_scores = np.array([val for kvp in target.values() for sub, val in kvp.items() \
                                    if sub in common_ranked_items])
    
    compare_rated_scores =  np.array([simdata.data[comp_one][common_ranked_items[i]] \
                                      for i in range(len(common_ranked_items))])
    
    diff = target_rated_scores - compare_rated_scores
      
    squr = diff*diff
    
    sum_of_squr = sum([squr.tolist()[i] for i in range(len(squr))])
        
    return 1/(1+ math.sqrt(sum_of_squr))    

def Euclidean_similarity_matrix(target):
    comp_names = [name for name in simdata.data.keys()]
        
    reg_dist = [Euclidean_similarity(target, comp_names[i]) for i in range(len(comp_names))]
  
    return reg_dist

def Pearson_similarity(target, comp_name):
    common_ranked_items = [itm for key in target.values() for itm in key.keys() \
                           if itm in simdata.data[comp_name].keys()]
    
    mu1 = sum([val for name, itm in target.items() for sub, val in itm.items() \
         if sub in common_ranked_items]) / len(common_ranked_items)
    
    mu2 = sum([simdata.data[comp_name][common_ranked_items[i]] \
               for i in range(len(common_ranked_items))])/len(common_ranked_items)
    
    ra = np.array([val for itm in target.values() for sub, val in itm.items() \
                   if sub in common_ranked_items])
    
    ru = np.array([simdata.data[comp_name][common_ranked_items[i]] \
                   for i in range(len(common_ranked_items))])
    
    diff_ra = ra-mu1*np.ones(len(ra))
    diff_ru = ru-mu2*np.ones(len(ru))
    
    num = sum((diff_ra)*(diff_ru))
    den = math.sqrt(sum(diff_ra**2)*sum(diff_ru**2))
    
    return num/(1 +den) #為了不讓分母有為0的機會，所以加上1

def Pearson_similarity_matrix(target):
    comp_names = [name for name in simdata.data.keys()]
    output = [Pearson_similarity(target, comp_names[i]) for i in range(len(comp_names))]
    return output


def recommander_score(target, ref_score, threshold, similarity_method):
    similarity_vector = similarity_method(target)
    sim_of_selected_people = [similarity_vector[i] for i in range(len(similarity_vector)) \
                              if similarity_vector[i] >= threshold]
    
    weight = sum(sim_of_selected_people[i] * ref_score[i] for i in range(len(sim_of_selected_people)))

    return weight / sum(sim_of_selected_people)


