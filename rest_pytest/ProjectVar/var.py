#encoding = utf-8
import os

project_path = os.path.dirname(os.path.dirname(__file__))
project_path = project_path.replace('\\','/')
test_data_path= project_path+u"/TestData/data.xlsx"
log_path=project_path+u'/Log/'

if __name__=='__main__':
    print(os.path.exists(project_path))
    print(os.path.exists(page_object_repository_path))
    print(project_path)
    print(page_object_repository_path)
