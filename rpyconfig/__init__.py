import os
import json
import argparse

env = os.environ.get('env') or 'default'

parser = argparse.ArgumentParser()
parser.add_argument("--environment", "-env", help="Environment to use", default=env)
parser.add_argument("--config", "-c", help="Configuration to use", default="")
args = parser.parse_args()



class Objectify:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                f = Objectify(value)
                self.__dict__.update({key: f})
            elif isinstance(value, list):
                t = []
                for i in value:
                    t.append(Objectify(i)) if isinstance(i, dict) else t.append(i)
                self.__dict__.update({key: t})
            else:
                self.__dict__.update({key: value})

# -- Deprecated --
# class DictToObject(object):
#     def __init__(self, dictionary):
#         for key, value in dictionary.items():
#             if type(value) == dict:
#                 setattr(self, key, DictToObject(value))
#             else:
#                 setattr(self, key, value)


class Config:
    __instance__ = None

    def __init__(self, args):
        self.args = args
        self.current = self.get_config()
        if Config.__instance__ == None:
            Config.__instance__ = self


    def get_config(self):
        environment = self.args.environment
        config = "-%s" % self.args.config if self.args.config else ""

        cwd = os.getcwd()

        specific_config_file = os.path.abspath(cwd + "/config/%s%s.json" % (environment, config))
        env_config_file = os.path.abspath(cwd + "/config/%s.json" % (environment))

        # Try to use the <env>-<conf> file
        conf = os.path.exists(specific_config_file) and open(specific_config_file)
        # If <env>-<conf> file doesn't exist, use the <env> file
        if not conf: conf = open(env_config_file)

        # Make the json config a nested object
        configuration = Objectify(json.load(conf))

        return configuration


    @staticmethod
    def get_instance():
        result = object
        if Config.__instance__ != None and hasattr(Config.__instance__, 'current'):
            result = Config.__instance__.current

        return result

Config(args)
config = Config.get_instance()
