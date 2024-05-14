import zipfile

def readdata(path):
    if '.zip' in path.name:
        print('that\'s a zip!')
        try:
            test = zipfile.ZipFile(path, 'r')
            return_data = []
            for filename in test.namelist():
                with zipfile.ZipFile(path) as my_zip:
                    with my_zip.open(filename) as data:
                        return_data.append(data.read())
            return return_data
        except:
            print('unzip error')
    try:
        with path.open('r') as file:
            data = file.read()
            return data
    except:
        if path.is_file():
            print('File exists but read error.')
        elif path.is_dir():
            print('Directory exists. Please input file and not dir.')
        elif path.exists():
            print('Path exists, but unexpected error.')
        elif not path.exists():
            print('Path does not exist.')

#def parsed_data(path):