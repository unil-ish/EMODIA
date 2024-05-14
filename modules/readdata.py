def readdata(path):
    with path.open('r') as file:
        data = file.read()
        return data
