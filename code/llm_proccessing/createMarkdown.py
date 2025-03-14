import re

from mdutils import MdUtils


def write_docs(mdFile, level: int, response, typescript:bool):
    """
    Recursively writes markdown documentation using the provided array of responses
    :param mdFile: the markdown object to write
    :param level: the level of heading of this array
    :param response: the array of responses to doccument
    :param typescript: If true only typescript files will be imported if false only javascript ones will
    :return: void
    """

   # whether code should be wrapped in a typescript of javascript block.
    if typescript:
        ending = "ts"
    else:
        ending = "js"
    # prevents recursion issues as max level is 6 for headings.
    if level > 4:
        level = 4
    first = True
    for value in response:
        if first:
            first = False
        else:
            # line break between items in lists so its obvious they're separate items
            mdFile.write("\n\n --- \n")
        my_keys = value.keys()
        for key in my_keys:
            # making names have space eg. TestCase -> Test Case
            heading_key = re.sub(r"(\w)([A-Z])", r"\1 \2", key)
            if key != "Name":
                mdFile.new_header(level=level+1, title=heading_key, add_table_of_contents="n")
            if isinstance(value[key], list):
                write_docs(mdFile=mdFile, level=level + 2, response=value[key], typescript=typescript)
            elif isinstance(value[key], dict):
                write_docs(mdFile=mdFile, level=level + 2, response=[value[key]], typescript=typescript)
            else:
                # Keyword for creating a codeblock
                if key == "Code" or key == "ExampleUse":
                    mdFile.write("```"+ending+" \n" + value[key] + "\n```")
                #Every dictionary has a name and looks better when heading is the name itself and not "Name"
                elif key == "Name":
                    mdFile.new_header(level=level, title=value[key], add_table_of_contents="n")
                else:
                    mdFile.new_paragraph(value[key])


def create_markdown(package, responses, outputdir, typescript):
    """
    creates the markdown file with structed llm responses
    :param package: package name for title
    :param responses: structured llm responses as list
    :param outputdir: output directory of markdown docs
    :param typescript: If true only typescript files will be imported if false only javascript ones will
    :return:
    """
    mdFile = MdUtils(file_name=outputdir, title=package + " Documentation")
    level = 2
    write_docs(mdFile, level, responses, typescript)
    mdFile.create_md_file()
