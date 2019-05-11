# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:00:58 2019

@author: Owner
"""
import time
start = time.time()
with open("nissle_genom.txt","r") as file:
    gene_seq = file.read()
    
def scoring(sequence1,sequence2):
    score =0
    for i in range(len(sequence1)):
        if sequence1[i]==sequence2[i]:
            score+=1
    return score 
                
def search_similar_seq(sequence1,similarity): #similarity ranges from 0 to 1 
    i=0
    length =len(sequence1)
    potential_list =[]
    while i+length <len(gene_seq):
        sequence2 = gene_seq[i:i+length]
        if len(sequence2) == length:
            score = scoring(sequence1,sequence2)
            if score >= length*similarity: 
                potential_list.append(i)
            i += 1
    return len(potential_list), potential_list


seq1 = 'gacactggggacatcgcgg'
print (search_similar_seq(seq1,0.8))
end = time.time()
print(end-start)
        
        