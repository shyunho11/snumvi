import pandas as pd
import re
import os
import glob
import pydicom
import csv

data_dir = "D:/Desktop/dicom"
df = pd.read_excel("D:/Desktop/adata_after2018_230518.xlsx", usecols="B,I").set_index("Number_폴더이름")

def normal_str(string):
    return re.sub("[^0-9a-z]", "", string.lower())

def find_ser(patient_id):
    print(patient_id, end=" :\t")
    
    if not os.path.exists(os.path.join(data_dir, str(patient_id))):
        print("Directory not found")
        return None
    
    target_ser = normal_str(df.loc[patient_id, 'MRI 20MIN 실제 이름들'])    
    dcm_files = glob.glob(os.path.join(data_dir, str(patient_id)) + '/*00001.dcm')

    if not dcm_files:
        dcm_files = glob.glob(os.path.join(data_dir, str(patient_id)) + '/*.dcm')
        target_files = []

        for dcm_file in dcm_files:
            dcm_data = pydicom.dcmread(dcm_file)
            series_desc = normal_str(dcm_data.SeriesDescription)
            if target_ser == series_desc:
                target_files.append(os.path.basename(dcm_file))

        print(f'Manually collected - {len(target_files)} files')
        return target_files
            
    if target_ser[:2] == 'ti':
        target_ser = 't1' + target_ser[2:]
    elif patient_id == 263:
        target_ser = 'itrcsvibeacc16traiso1mm20min'
    elif patient_id == 294:
        target_ser = '3daxialt1wifs20min'

    for dcm_file in dcm_files:
        dcm_data = pydicom.dcmread(dcm_file)
        series_n = dcm_file.split('ser')[1].split('img')[0]
        series_desc = normal_str(dcm_data.SeriesDescription)
        if target_ser == series_desc:
            print(series_n, series_desc)
            return 'ser' + series_n
    
    print("Failed to search")
    return -1

ser_found = []

for patient_id in df.index:
    ser_found.append(find_ser(patient_id))

df['ser'] = ser_found




df.to_csv("D:/Desktop/ser_found.csv")

df2 = df.loc[df['ser'] == -1]

for patient_id in df2.index:
    target_ser = df2.loc[patient_id, 'MRI 20MIN 실제 이름들']
    dcm_files = glob.glob(os.path.join(data_dir, str(patient_id)) + '/*00001.dcm')
    print("-"*50)
    print("patID: ", patient_id)
    print("MRI 20MIN 실제 이름: ", target_ser)
    for dcm_file in dcm_files:
        dcm_data = pydicom.dcmread(dcm_file)
        series_n = dcm_file.split('ser')[1].split('img')[0]
        series_desc = dcm_data.SeriesDescription
        print(series_n, series_desc)