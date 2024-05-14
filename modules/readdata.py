def readdata(path):
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


