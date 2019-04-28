# -*- coding: utf-8 -*-


with open("nissle_genom.txt","r") as file:
    gene_seq = file.read()
    def pre_gene_sequence(gene, length):
        i=0
        potential_list =[]
        while i < len(gene_seq):
            gene_index = gene_seq.find(gene,i)
            if gene_index==-1: 
                if len(potential_list)==0:
                    return "can not find the gene sequence"
                else:
                    return potential_list
            else: 
                potential_list.append(gene_seq[gene_index-1-length:gene_index-1])
                i = gene_index+1
    print (pre_gene_sequence("tttcgccaaaatc",20))
 
    
    def frequency(sequence):
        i=0
        n=0
        while i < len(gene_seq):
            gene_index = gene_seq.find(sequence,i)
            if gene_index==-1:
                return n 
            else:
                i = gene_index+1
                n+=1
                
    print(frequency("tttcgccaa"))
                
        
        
    

        
        
        
    



    


