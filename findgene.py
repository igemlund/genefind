# -*- coding: utf-8 -*-

with open("nissle_genom.txt","r") as file:
    gene_seq = file.read()

    def pre_gene_sequence(gene, length):
        gene_index = gene_seq.find(gene)
        if gene_index==-1:           
            return "can not find the gene sequence"
        else:
            return gene_index, gene_seq[gene_index-1-length:gene_index-1]
            
    print (pre_gene_sequence("ggttttcttcaccagatccagcgccccccc",20))
    


