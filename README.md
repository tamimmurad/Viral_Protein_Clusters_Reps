# Viral Proteins Cluster Representative Proteins
Note: This part was later ignored as the NCBI cluster database covers only around 26,000 viral proteins. Please refere to https://github.com/tamimmurad/viral_protein_clustering to find how a more comprehensive clustering was performed.
## Description
This repository contains python scripts to get one protein (representative) for each protein clusters in viruses from NCBI clusters DB.
Also, one text file with all viral protein clusters Cluster_ACCNs.txt and the resulting reps in rep_Proteins.csv.
The data was extracted from the NCBI Protein Clusters DB data available and can be found under the link:
https://ftp.ncbi.nih.gov/genomes/CLUSTERS/




## Scripts

### Script Name: protein_cluster_ACCN.py

#### Description:

This Python code retrieves a list of protein clusters' Accession numbers (ACCNs) for a specific 
taxonomic group by using the txid from the NCBI protein clusters database. 


### Script Name: protein_clusters_reps.py

#### Description: 

This script is written with the aim of extracting a representative protein (largest protein in terms of sequence length) for 
a desired cluster(s). It uses two tabular files where the first files contains a list of proteins with each row containing at least
protein ACCN, its cluster ACCN and its length. The 2nd file contains a list of all desired clusters in a column.
It outputs a CSV file with the columns: Cluster ACCN, representative protein ACCN and 4 additional parameters including sequence length.
