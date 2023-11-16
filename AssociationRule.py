# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:13:50 2023

@author: lEO
"""

import warnings
from mlxtend.frequent_patterns import apriori, association_rules
from DataPreprocessing import EncodedDatasetAssociationRule, EncodedDatasetAssociationRule2014, EncodedDatasetAssociationRule2015

warnings.filterwarnings("ignore")        
        
# -----> ASSOCIATION RULE 2014 to 2015
support = apriori(EncodedDatasetAssociationRule, min_support = 0.003, use_colnames = True)
confidence = association_rules(support, metric = "confidence", min_threshold = 0.01)       
lift = association_rules(support, metric = "lift", min_threshold = 1.0)      



# -----> ASSOCIATION RULE 2014
support2014 = apriori(EncodedDatasetAssociationRule2014, min_support = 0.005, use_colnames = True)
confidence2014 = association_rules(support2014, metric = "confidence", min_threshold = 0.01)       
lift2014 = association_rules(support2014, metric = "lift", min_threshold = 1)    



# -----> ASSOCIATION RULE 2015
support2015 = apriori(EncodedDatasetAssociationRule2015, min_support = 0.005, use_colnames = True)
confidence2015 = association_rules(support2015, metric = "confidence", min_threshold = 0.01)       
lift2015 = association_rules(support2015, metric = "lift", min_threshold = 1.0)           
        

        
        
        
        
        
        