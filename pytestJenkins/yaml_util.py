import yaml


class ReadYaml:
    def __init__(self,filename):
        self.filename = filename

    def readYaml(self):
        with open(self.filename,'r',encoding='utf-8') as rfile:
            params = yaml.load(rfile,Loader=yaml.FullLoader)
            return params

if __name__ == '__main__':
    ReadYaml('test01.yaml').readYaml()