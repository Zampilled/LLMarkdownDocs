import os


def get_files(node_package: str):
    """
    Retrieves codebase of given node package to be fed into LLM
    :param node_package: name of installed node package
    :return: codebase as string
    """
    my_code = ""
    root = 'node_modules/' + node_package
    search = []

    for path, _, files in os.walk(root):
        for name in files:
            search.append(os.path.join(path, name))

    for file in search:
        f = open(file, 'r')
        my_code += "\n" + file + "\n"
        my_code += f.read()
        my_code += "\n ENDFILE \n"
        f.close()

    return my_code
