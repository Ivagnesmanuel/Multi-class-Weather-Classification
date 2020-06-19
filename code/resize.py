from PIL import Image
import os, sys

def resize(path, dirs, out):
    for item in dirs:
        if os.path.isfile(path+'/'+item):
            im = Image.open(path+'/'+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((150,150), Image.ANTIALIAS)
            imResize.save(out + '/' + item,  'PNG', quality=90)

path1 = '../dataset_3200/HAZE'
path2 = '../dataset_3200/SUNNY'
path3 = '../dataset_3200/RAINY'
path4 = '../dataset_3200/SNOWY'

resize(path1, os.listdir( path1 ), 'HAZE')
print('HAZE done')
resize(path2, os.listdir( path2 ), 'SUNNY')
print('SUNNY done')
resize(path3, os.listdir( path3 ), 'RAINY')
print('RAINY done')
resize(path4, os.listdir( path4 ), 'SNOWY')
print('SNOWY done')
