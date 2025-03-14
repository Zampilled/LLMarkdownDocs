import argparse
from tqdm import tqdm


from llm_proccessing.createMarkdown import create_markdown
from llm_proccessing.getFiles import get_files
from llm_proccessing.getLLMResponse import get_llm_response

from ast import literal_eval

def main(package,exports, outputdir, model, typescript):
    """
    Main function for creating markdown docs for a npm package using the exports
    :param package: name of package to be documented
    :param exports: array of exports to be documented
    :param outputdir: output directory for the markdown files
    :param model: name of the model to be used
    :param typescript: If true only typescript files will be imported if false only javascript ones will
    :return: void
    """
    codebase = get_files(package, typescript)
    data = []
    for method in tqdm(exports):
        tqdm.write(method+" export being documented")
        response = get_llm_response(method, codebase, model).model_dump_json()
        response_dict = {"Name": method}
        response_dict.update(literal_eval(response))
        data.append(response_dict)
    create_markdown(package, data, outputdir, typescript)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--package", help="The package name")
    parser.add_argument("-o","--outputdir", help="The markdown output directory")
    parser.add_argument("-m","--model", help="model to be used")
    parser.add_argument("-e","--export", help="The export names seperated by space")
    parser.add_argument("-t","--typescript", help="If true only typescript files will be imported if false only javascript ones will")
    args = parser.parse_args()
    main(args.package,args.export.split(" "), args.outputdir, args.model, args.typescript)