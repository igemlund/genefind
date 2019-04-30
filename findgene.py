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
                
    def freq_pre_gene(gene,length):
        potential_list = pre_gene_sequence(gene,length)
        freq_list = []
        if type(potential_list) == "list":
            for i in potential_list:
                freq_list.append(frequency(i))
            return potential_list, freq_list
        else:
            return "can not find the gene sequence"
        
    print (freq_pre_gene("tttaaaatatq",10))
    

                
        
        
    

        
        
        
    



    


