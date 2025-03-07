from typing import List

from pydantic import BaseModel


class Parameter(BaseModel):
    name: str
    type: str
    description: str

class ReturnValue(BaseModel):
    name: str
    type: str
    description: str

class TestCase(BaseModel):
    name: str
    description: str
    code: str

class NPMExport(BaseModel):
    description: str
    parameters: List[Parameter]
    return_value: ReturnValue
    example_use: str
    test_cases: List[TestCase]


ollama_model: str = "tinyllama"

my_prompt: str = """
You are an expert NodeJS export documentation writer. 
For each export you create a description, document parameters, document the return value, 
create and example_use to be used as an example of the export, and some relevant test cases tha can 
be used to test the export in a meaningful way. 
Your job is to take the method immediately proceeding this sentence and 
use the codebase after it to create extensive documentation for that export.
"""


