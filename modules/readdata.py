import zipfile


def readdata(path, **kwargs):
    if '.zip' in path.name:
        if not kwargs["zip_name"]:
            print('Please select a zip file.')
            return
        zip_name = kwargs['zip_name']
        print(f'desired file in zip: {zip_name}')
        print('that\'s a zip!')
        try:
            test = zipfile.ZipFile(path, 'r')
            return_data = []
            print(test.namelist())
            #for filename in test.namelist():
            #    with zipfile.ZipFile(path) as my_zip:
            #        with my_zip.open(filename) as data:
            #            return_data.append(data.read())
            with zipfile.ZipFile(path, 'r') as my_zip:
                with my_zip.open(zip_name) as data:
                    return_data = data.read()

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

# def parsed_data(path):
