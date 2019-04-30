# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:18:35 2019

@author: Owner
"""

with open("nissle_genom.txt","r") as myfile:
    gene_seq = myfile.read()
    new_gene_seq = gene_seq.replace("\n","")
    with open("nissle_genom.txt","w") as afile:
        afile.write(new_gene_seq)
    