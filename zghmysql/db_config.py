import configparser
#把登录的过程写入配置文件进行读取调用，写成类
class readConfig:
    def read_config(self,conf_path,section,option):
        tt = configparser.ConfigParser()
        tt.read(conf_path)#假设有两万行代码
        result= eval(tt.get(section,option))
        return result

    def get_config_new(conf_path,section,option):
        tt = configparser.ConfigParser ()
        tt.read (conf_path)
        config = eval (tt.get (section, option))
        return config
        #print('调用结束')