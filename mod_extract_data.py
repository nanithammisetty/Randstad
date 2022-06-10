import pandas as pd
import sys
class cls_extract_data:
    def method1(self,data_to_extract):
        extracted_data=pd.read_csv(data_to_extract)
        return extracted_data
