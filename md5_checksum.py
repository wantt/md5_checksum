# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:08:50 2018

@author: os
"""
#%%
import os
import hashlib




def md5sum(filename,block_size=2**20):
    md5=hashlib.md5()
    try:
        with open(filename,'rb') as file:
            while True:
                data = file.read(block_size)
                if not data:
                    break
                md5.update(data)
                
    except IOError:
        print(filename+"not found")
    except:
        return None
    return md5.hexdigest()
    
#%%
all_md5=[]
base_dir =r"D:\DATA_SURESENCE\suresence\all_kind_kws"
for path,pathname,filenames in os.walk(base_dir):
    for filename in filenames:
        tmp_md5=md5sum(os.path.join(path,filename))
        if not tmp_md5 in all_md5:
            all_md5.append(tmp_md5)
        else:
            os.popen('del "%s"'%(os.path.join(path,filename)) )

    