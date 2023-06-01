import os
import glob
import pandas as pd
import nibabel as nib

data_dir = 'D:\Desktop\최종IN_N=248'
nifti_dir = 'D:\Desktop\HBP'

def get_l_center(data_dir):
    jpg_files = glob.glob(os.path.join(data_dir, '*.jpg'))
    result = {}

    for file in jpg_files:
        filename = os.path.basename(file).split('_')
        patID = int(filename[0])
        l_center = int(filename[-1].split('.')[0])
        result[patID] = l_center

    return result

def get_nifti_shape(df, nifti_dir):
    result = []

    for i in df.index:
        filename = os.path.join(nifti_dir, str(i) + '.nii.gz')
        l_size = None

        try:
            nimg = nib.load(filename)
            l_size = nimg.get_fdata().shape[-1]
        except:
            print("Failed to open {}".format(filename))

        result.append(l_size)
    
    return result

df = pd.DataFrame.from_dict(get_l_center(data_dir), orient='index', columns=['l_center']).sort_index()

df['l_size'] = get_nifti_shape(df, nifti_dir)
df.insert(1, 'l_center_inverse', df['l_size'] - df['l_center'])
df.to_csv("D:/Desktop/l_center.csv")