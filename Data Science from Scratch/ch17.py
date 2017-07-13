# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:51:53 2017

@author: 2017041801
"""

import math
from collections import Counter
from collections import defaultdict
from functools import partial

def entropy(class_probabilities):
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)

def class_probabilities(labels): #probability of y's class(T / F)
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets) #總筆數:14
    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)
    
def sort_partition_by(atttribute, inputs): #依據屬性進行排序
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][atttribute]
        groups[key].append(input)
    return groups    

def partition_entropy_by(attribute, inputs):
    partition = sort_partition_by(attribute, inputs)
    return partition_entropy(partition.values())

inputs = [
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False),
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False),
        ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True),
        ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False),
        ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True),
        ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True),
        ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False)
    ]


def build_tree_id3(inputs, split_candidates=None):
    # 沒給候選項就從訓練資料理面抓
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()
        
    num_inputs = len(inputs)
    num_trues = len([cat for att, cat in inputs if cat])
    num_falses = num_inputs - num_trues
    
    if num_trues == 0: return False
    if num_falses == 0: return True
    
    if not split_candidates:
        return num_trues >= num_falses
    
    best_att = min(split_candidates, key=partial(partition_entropy_by, inputs=inputs))
    
    sorted_partitions = sort_partition_by(best_att, inputs)
    new_candidates = [a for a in split_candidates if a != best_att]
    
    subtrees = {att_v : build_tree_id3(subset, new_candidates) for att_v, subset in sorted_partitions.items()}
    
    subtrees[None] = num_trues > num_falses
               
    return (best_att, subtrees)

def classify(tree, input):
    if tree in [True, False]:
        return tree
    att, subtree_dict = tree
    
    subtree_key = input.get(att)
    
    if subtree_key not in subtree_dict:
        subtree_key = None
    
    subtree = subtree_dict[subtree_key]
    
    return classify(subtree, input)

dataSet = [({'a1':1, 'a2':1}, True),
           ({'a1':1, 'a2':1}, True),
           ({'a1':1, 'a2':0}, False),
           ({'a1':0, 'a2':1}, False),
           ({'a1':0, 'a2':1}, False)]

tree = build_tree_id3(inputs, ['level', 'lang', 'tweets', 'phd'])
print(tree)
"""
print(classify(tree, { "level" : "", 
                 "lang" : "Java", 
                 "tweets" : "yes", 
                 "phd" : "no"} )
     )
"""
#senior_input = [(att, lab) for att, lab in inputs if att['level'] == 'Junior']
#print(senior_input)
"""
for key in ['lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(key, senior_input))
"""


#gps = partition_by('level', inputs)
#print([len(subset) for subset in gps.values()])
#print([label for subset in gps.values() for _, label in subset])
#pe = partition_entropy_by('level', inputs)
#print(pe)
#pb = [({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True), ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True), ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, False), ({'level': 'Junior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'no'}, True), ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False)]
#lab = [label for _, label in pb]
#print(lab)
#print(class_probabilities(lab))
