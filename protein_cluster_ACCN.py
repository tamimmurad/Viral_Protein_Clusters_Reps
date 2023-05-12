#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: protein_cluster_ACCN.py

Description:

This Python code retrieves a list of protein clusters' Accession numbers (ACCNs) for the  
taxonomic group of viruses (txid=10239) from the NCBI protein clusters database. 

Functions: get_cACCN(clusterID,idList)

Procedure:
    
    1. Importing the required libraries: Bio and re.
    2. Providing an email address to NCBI.
    3. Defining the taxonomic ID, here "txid10239" representing viruses.
    4. Using the Entrez.esearch function to search for the taxonomic ID in the proteinclusters database.
    5. Parsing the search results using Entrez.read function.
    6. Extracting the cluster IDs from the search results.
    7. Iterating over the cluster IDs to get the matching ACCNs and storing them in a list.
    8. Writing the cluster ACCNs to a text file. 
    
Input: None. Tax ID and email address to be specified in the script.
Output: Text file with a list of potein clusters' ACCNs.

Version 1.00
Date: April 12th, 2023
Author: ChatGPT, reviewed and corrected by Tamim AlMurad
"""

from Bio import Entrez
import re

# Provide your email address to NCBI to identify yourself
Entrez.email = "xxx"

# Define the cluster ID you want to retrieve protein list for. In this case it is viruses taxID.
taxID = "txid10239"

# Use Entrez.esearch to search for the cluster ID in the protein clusters database.
handle = Entrez.esearch(db="proteinclusters", term=f"{taxID}[organism]",retmax=10000)

# Parse the search results with Entrez.read
record = Entrez.read(handle)

# Get the cluster ids and store them in a list of strings without unwanted characters.
clusterIDs = re.sub("'","",str(record["IdList"])).replace('[','').replace(']','').split(', ')

# Initialize an empty list for the clusters' ACCNs.
clusterACCNs =[]


# Function get_cAAN gets the cluster ACCN from the cluster ID and store it in a list.
def get_cACCN(clusterID,idList):
    
    # Use Entrez.efetch to get the cluster summary and parse it.
    handle = Entrez.efetch(db="proteinclusters", id=clusterID,rettype="docsum")
    record=Entrez.read(handle)
    
    # Closing the handle
    handle.close()
    # Append found ACCN to the list.
    idList.append(str(record[0]['ACCN']))
    


# Iterate over clusters' IDs to get clusters' ACCNs 
for clusID in clusterIDs:
    get_cACCN(clusID,clusterACCNs)
    # Debugging only to see the progress.
    print('The number of finished IDs are %d ' %len(clusterACCNs))
   

# Write the cluster ACCNs in a txt file.
file = open('Cluster_ACCNs.txt','w')
file.write('\n'.join(clusterACCNs))
file.close()

