import os
import pandas as pd
from mod_extract_data import cls_extract_data

class base_process_data:
    def fetch_data(self):

        return 0
    def get_shape(self):

        return 0
    def clean_data_for_nulls(self):
        return 0
    def select_imp_columns(self,dataframes):

        return 0
class process_data_elem(base_process_data):
    def fetch_data(self,element_data_file):
        sol = cls_extract_data()
        element_data=sol.method1("C:/Users/venu/OneDrive/Desktop/Prior_to_join/test_data/"+element_data_file)
        return element_data
    def get_shape(self,element_data):
        element_shape=element_data.shape
        return element_shape
    def clean_data_for_nulls(self,element_data):
        cleaned_elem=element_data.dropna()
        return cleaned_elem
    def select_imp_columns(self,cleaned_elem):
        elem_keys=cleaned_elem.keys()
        return elem_keys

class process_data_secd(base_process_data):
    def fetch_data(self,secd_data_file):
        sol = cls_extract_data()
        secd_data=sol.method1("C:/Users/venu/OneDrive/Desktop/Prior_to_join/test_data/"+secd_data_file)
        return element_data
    def get_shape(self,secd_data):
        sced_shape=secd_data.shape
        return secd_shape
    def clean_data_for_nulls(self,secd_data):
        cleaned_secd=secd_data.dropna()
        return cleaned_secd
    def select_imp_columns(self,cleaned_secd):
        secd_keys=cleaned_secd.keys()
        return secd_keys