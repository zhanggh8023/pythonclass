
import configparser

class config:
    def read_config(self,conf_path,section,option):
        rc=configparser.RawConfigParser()
        rc.read(conf_path,encoding='utf-8')
        result=rc.get(section,option)
        return result