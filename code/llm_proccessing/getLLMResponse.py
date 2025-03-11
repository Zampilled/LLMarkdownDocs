from ollama import generate

import config as config

prompt = config.my_prompt
NPMExport = config.NPMExport

def get_llm_response(request_export, codebase, model):
    """
    Gets response from LLM given a structure defined in config
    :param request_export: the export to query
    :param codebase: the codebase of the package
    :param model: the model to be used to generate the response
    :return: structured LLM response
    """
    response = generate(
        prompt=prompt + request_export + codebase,
        model=model,
        format=NPMExport.model_json_schema(),
    )
    method_docs = NPMExport.model_validate_json(response.response)
    return method_docs
