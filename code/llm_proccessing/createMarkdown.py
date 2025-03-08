import re

from mdutils import MdUtils


def writeDocs(mdFile, level: int, response):
    # prevents recursion issues
    if level > 6:
        level = 6
    myLevel = level
    first = True
    for value in response:
        if first:
            first = False
        else:
            mdFile.write("\n\n --- \n")
        my_keys = value.keys()
        for key in my_keys:
            headingKey = re.sub(r"(\w)([A-Z])", r"\1 \2", key)
            if key != "Name":
                mdFile.new_header(level=myLevel + 1, title=headingKey, add_table_of_contents="n")
            if isinstance(value[key], list):
                writeDocs(mdFile=mdFile, level=myLevel + 2, response=value[key])
            elif isinstance(value[key], dict):
                writeDocs(mdFile=mdFile, level=myLevel + 2, response=[value[key]])
            else:
                if key == "Code" or key == "ExampleUse":
                    mdFile.write("```js \n" + value[key] + "\n```")
                elif key == "Name":
                    mdFile.new_header(level=myLevel, title=value[key], add_table_of_contents="n")
                else:
                    mdFile.new_paragraph(value[key])


def createMarkdown(package, responses, outputdir):
    mdFile = MdUtils(file_name=outputdir, title=package + " Documentation")
    level = 2
    writeDocs(mdFile, level, responses)
    mdFile.create_md_file()
