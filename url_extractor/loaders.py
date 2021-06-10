from os import listdir
from os.path import isfile, join, dirname

DIRNAME = dirname(__file__)
FILTER_PATH = join(DIRNAME, 'filter/')
FILES_PATH = join(DIRNAME, 'files/')

def load_filters():
    filter = [[],[]]
    filter_list = []
    print('> Loading filters..')
    partial = [f for f in listdir(FILTER_PATH) if isfile(join(FILTER_PATH, f))]
    for i in range(len(partial)):
        filter_list.append('{}'.format(partial[i]))
        with open('{}{}'.format(FILTER_PATH, partial[i])) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
        for j in range(len(content)):
            aux = content[j].split('.')
            filter[0].append(aux[0])
            filter[1].append(aux[1])
        filter[0] = list(dict.fromkeys(filter[0]))
        filter[1] = list(dict.fromkeys(filter[1]))
        del content
    return filter

def load_files():
    print('> Loading files..')
    result = []
    files = [f for f in listdir(FILES_PATH) if isfile(join(FILES_PATH, f))]
    for i in range(len(files)):
        result.append('{}'.format(files[i]))
    print('> Loading complete! {} files found'.format(len(result)))
    return result