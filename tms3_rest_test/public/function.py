# -*- coding: utf-8 -*-
from selenium import webdriver
import os

def Screenshot_img(driver,dir_name,file_name):
    '''
    截图
    获取存储路径，脚本在test_case中，图片存储在与test_case平级的result下image中
    '''
    file_path=get_filepath("/result/image/")

    #对每一个test，创建一个文件夹下存储截图，文件夹名称自定义
    if not os.path.exists(file_path + dir_name):
        os.mkdir(file_path + dir_name)

    file_path=file_path+dir_name+'/'+file_name +'.jpg'
    driver.get_screenshot_as_file(file_path)


def get_filepath(subpath):
    '''获取文件存储路径'''
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/interface')[0]
    file_path=base+subpath
    return file_path

if __name__=='__main__':
	driver = webdriver.Firefox()
	driver.get("https://www.baidu.com")
	Screenshot_img(driver,time.strftime('%Y-%m-%d %H%M%S')+'baidu.jpg')
	driver.quit()
