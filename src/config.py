import yaml

def load_config():
    with open("config.yaml", "r") as conf:
        return yaml.load(conf, Loader=yaml.FullLoader)