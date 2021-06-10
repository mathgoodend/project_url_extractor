import re
from .loaders import load_filters

def extractor(data, nofilters = False):
    if nofilters is True:
        url_regex = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    else:
        filter = load_filters()
        regex = [
            r"(?i)\b((?:https?:\/\/(.+?\.)?(",
            r"|".join('{}'.format(k) for k in filter[0]),
            r")\.(?:",
            r"|".join('{}'.format(k) for k in filter[1]),
            r")(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])))"
        ]
        url_regex = re.compile('{}{}{}{}{}'.format(regex[0],regex[1],regex[2],regex[3],regex[4]), re.VERBOSE)
    urls = re.findall(url_regex, data)
    return urls