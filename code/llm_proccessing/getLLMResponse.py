from ollama import generate

import config as config

prompt = config.my_prompt
NPMExport = config.NPMExport
llm = config.ollama_model


def getLLMResponse(request_method, codebase):
    response = generate(
        prompt=prompt + request_method + codebase,
        model=llm,
        format=NPMExport.model_json_schema(),
    )
    method_docs = NPMExport.model_validate_json(response.response)
    return method_docs
