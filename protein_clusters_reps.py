# -*- coding: utf-8 -*-
"""
Script Name: protein_clusters_reps.py

Description: 

This script is written with the aim of extracting a representative protein (largest protein in terms of sequence length) for 
a desired cluster(s). It uses two tabular files where the first files contains a list of proteins with each row containing at least
protein ACCN, its cluster ACCN and its length. The 2nd file contains a list of all desired clusters in a column.
It outputs a CSV file with the columns: Cluster ACCN, representative protein ACCN and 4 additional parameters including sequence length.

packages invloved: pandas and time.

Procedure:
    
After importing required packages.    
    1. Starts by reading a file where the list of all proteins and the cluster they belong to are stored with 
    some additional information about the protein. This file is obtained by concatinating all the protein cluster files obtained 
    from NCBI Protein clusters database https://ftp.ncbi.nih.gov/genomes/CLUSTERS/ (only files with names ending with 
    "proteins" are needed). The file is read into a dataframe. 
    2. Read a file where the required protein clusters' accession numbers are stored into a list.
    3. Iterate over the clusters's ACCNs to find its proteins, sort these proteins descendingly by their sequence length, extrat 
    the longest one and append it to the results dataframe (clustReps).
    4. Write the resulting dataframe into a csv file named 'rep_proteins.csv'.

Input : 2 text files: proteins list file and target protein clusters files.
output: 1 CSV file with protein clusters representative proteins ACCNs.

Version 1.00
Date: April 12th, 2023
Author: Tamim AlMurad

"""




#%%
import pandas as pd
import time


# Read the proteins data into a dataframe.
clusterDF = pd.read_csv('./All clusters/all_clusters.txt',sep='\t')

#Debugging only.
print('Finished creating a dataframe \n')
#%%
# Read the required clusters ACCNs into a list.
cfile= open('Cluster_ACCNs.txt','r')
clusterACCNs = cfile.read().split()


#%%
#Timer starts.
start=time.time()

# Results dataframe.
clustReps = pd.DataFrame(columns=clusterDF.columns)

# Iterate over the clusters to get cluster reps.
for accn in clusterACCNs:
    clustReps=pd.concat([clustReps,clusterDF[clusterDF['#cluster']==accn].sort_values(by=['length'],ascending=False).head(1)])
    # #Debugging only.
    print('Done with cluster # %d ' % clusterACCNs.index(accn) +'with ACCN ' + accn)


# Write the results into a csv file.
clustReps.to_csv('rep_proteins.csv',sep='\t' ,index=False)

# Get the time and pring the job is done.
seconds = time.time()-start
print("Job is done in %d seconds !!!!" %seconds)


#%%
#import multiprocessing
#from functools import partial
# def pop_clust_prot(accn,dfIn):
#     dfOut=dfIn[dfIn['#cluster']==accn].sort_values(by=['length'],ascending=False).head(1)
#     print('cluster ' + accn)
#     return list(dfOut)
    
    


# func = partial(pop_clust_prot, clusterDF)
# if __name__ == '__main__':
    
    
#     pool_obj = multiprocessing.Pool(multiprocessing.cpu_count())
#     print('starting to start with %d cpus' % multiprocessing.cpu_count())
#     ans = pool_obj.map(func,clusterACCNs[0:100]) 
#     print('ending')
#     pool_obj.close()   

