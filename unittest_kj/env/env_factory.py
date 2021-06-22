import yaml
import os
class ReadConfig():
    def __init__(self):
        # self.curPath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # self.yaml1=os.path.join(self.curPath,"config\config.yaml")
        # self.f1=open(self.yaml1,"rb")
        with open(r"D:\project_python\wl\unittest_kj\config\config.yaml", "rb") as self.f1:
            # self.f1 = open(r"D:\project_python\wl\unittest_kj\config\config.yaml", "rb")
            self.conf_file=yaml.load(self.f1,Loader=yaml.FullLoader)#导入yaml文件
            self.username=self.conf_file['user1']['username']
            self.password=self.conf_file['user1']['password']
            self.url=self.conf_file['user1']['url']

# a=ReadConfig()
# print(a.username)