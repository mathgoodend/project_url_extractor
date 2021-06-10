import sys, datetime
from .loaders import DIRNAME, FILES_PATH, 
from .loaders import load_files
from .extractor import extractor
from .manual import user_manual

def main():
    args = sys.argv[1:]
    if len(args) > 0:
        if args[1].lower() == 'nofilter':
            print('> No filter option. The script will extract every url it finds.')
            NOFILTER = True
        else: 
            print('> Filter option. The script will extract only the url that matches the filters found in \'./filters/\'')
            NOFILTER = False
        if args[1].lower() == 'man' or args[1].lower() == 'manual':
            return user_manual()
    
    files = load_files()
    urls = []
    dt = datetime.datetime.now()
    id_code = dt.strftime('%H%M%S%y')
    try:
        open('{}/output_{}.txt'.format(DIRNAME, id_code), 'x')
    except:
        print("> File already exists")
        with open('{}/output_{}.txt'.format(DIRNAME, id_code), 'w') as file:
            file.write('')
        print("> File has been cleared")

    for i in range(len(files)):
        print('> File Number: {}'.format(i+1))
        with open('{}/{}'.format(FILES_PATH, files[i]), 'r', encoding='utf-8', errors='ignore') as file:
            data = file.read()
            matches = extractor(data, NOFILTER)
            print('> Number of matches: {}'.format(len(matches)))
            for j in range(len(matches)):
                urls.append(matches[j])
            del matches
    with open('{}/output_{}.txt'.format(DIRNAME, id_code), 'a') as output_file:
        for item in urls:
            output_file.write('{}\n'.format(item[0]))
    print('> {} urls extracted'.format(len(urls)))
    print('> Done! Archive \'output_{}.txt\' succesfully created'.format(id_code))

if __name__ == '__main__':
    main()