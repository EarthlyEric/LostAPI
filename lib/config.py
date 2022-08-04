import os
from configobj import ConfigObj

class config():
    config=ConfigObj(os.path.join('config.ini'))
    token=config['token']