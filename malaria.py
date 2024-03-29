# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:03:26 2020

@author: megha
"""
#%%
# This is a script for identifying the protein name for
# a given protein id by comparing the fasta files with
# the respective blastx run result file.
# prot_dict is a dictionary containing sequence ID's as keys and 
# protein names as values.
#%%
# create a dictionary of sequence ID's and protein names:
Print("This script generates an output file containing the FASTA sequence with the respective protein names")
prot_dict = dict()
with open("malaria.blastx.tab") as protein:
    pread = protein.readlines() #pread is a list
    for lines in pread:
        lines= lines.strip().split('\t')
        prot_dict[lines[0]] = lines[9]

# compare the sequence ID's and write to a separate file "output.txt"
# write only the protein sequences which aren't null
with open("malaria.fna") as seq:
    with open("output.txt", "w") as seqID:
        for line in seq:
            if '>' in line:
                seq_ID=line.split('\t')[0].lstrip('>')
                prot_name = prot_dict[seq_ID]
                skip_prot = prot_name == "null"
                if not skip_prot:
                    seqID.write(line.strip().replace('\t', " ") + ' protein='+ prot_name + '\n')
            else: 
                if not skip_prot:
                    seqID.write(line)
 


