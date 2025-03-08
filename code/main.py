import argparse
from tqdm import tqdm

from llm_proccessing.createMarkdown import createMarkdown
from llm_proccessing.getFiles import getFiles
from llm_proccessing.getLLMResponse import getLLMResponse

from ast import literal_eval

def main(package,methods, outputdir):
    package = "@rescui/use-glow-hover"
    methods = ["glowHoverEffect", "useGlowHover"]
    codebase = getFiles(package)
    data = []
    for method in tqdm(methods):
        tqdm.write(method+" export being doccumented")
        response = getLLMResponse(method,codebase).model_dump_json()
        response_dict = {"Name": method}
        response_dict.update(literal_eval(response))
        data.append(response_dict)
    createMarkdown(package,data, outputdir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--package", help="The package name")
    parser.add_argument("-o","--outputdir", help="The markdown output directory")
    parser.add_argument("-m","--methods", help="The method names")

    args = parser.parse_args()
    main(args.package,args.methods, args.outputdir )#.split(" "))