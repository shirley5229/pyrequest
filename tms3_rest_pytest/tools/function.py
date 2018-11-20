# -*- coding: utf-8 -*-
import os


def get_filepath(subpath):
    '''获取文件存储路径'''
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/interface')[0]
    file_path=base+subpath
    return file_path
    

if __name__=='__main__':
	get_filepath('')
