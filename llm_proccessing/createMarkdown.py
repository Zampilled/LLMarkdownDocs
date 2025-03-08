from mdutils import MdUtils

from config import my_prompt


def writeDocs(mdFile,level:int,response):
    # prevents recursion issues
    if level >6:
        level = 6
    myLevel = level
    print(myLevel)
    for value in response:
        my_keys = value.keys()
        for key in my_keys:
            mdFile.new_header(level=myLevel, title=key, add_table_of_contents="n")
            if isinstance(value[key], list):
                writeDocs(mdFile=mdFile,level=myLevel+1,response=value[key])
            elif isinstance(value[key], dict):
                writeDocs(mdFile=mdFile,level=myLevel+1,response=[value[key]])
            else:
                if key == "code":
                    mdFile.write("```js \n"+value[key]+"\n```")
                else:
                    mdFile.new_paragraph(value[key])
        mdFile.write("\n\n --- \n")





def createMarkdown(package, responses , outputdir):
    mdFile = MdUtils(file_name=outputdir,title=package+" Documentation")
    level = 2
    writeDocs(mdFile, level, responses)
    mdFile.create_md_file()