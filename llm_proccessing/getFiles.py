import os


def getFiles(node_package: str):
    my_code = ""
    root = 'node/node_modules/'+node_package
    search  = []

    for path, _, files in os.walk(root):
        for name in files:
            search.append(os.path.join(path, name))

    for file in search:
        f = open(file, 'r')
        my_code += "\n"+ file +"\n"
        my_code += f.read()
        my_code += "ENDFILE \n"
        f.close()

    return my_code