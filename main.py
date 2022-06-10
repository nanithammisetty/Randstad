

from mod_process_data import base_process_data
from mod_process_data import process_data_elem
import os
if __name__ == '__main__':
    element_data_file="2015_16_Statewise_Elementary.csv"
    ob3=process_data_elem()
    elem_data=ob3.fetch_data(element_data_file)
    print(ob3.select_imp_columns(elem_data))
    print(elem_data)
