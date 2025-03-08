from typing import List

from pydantic import BaseModel


class Parameter(BaseModel):
    Name: str
    Type: str
    Description: str

class ReturnValue(BaseModel):
    Name: str
    Type: str
    Description: str

class TestCase(BaseModel):
    Name: str
    Description: str
    Code: str

class NPMExport(BaseModel):
    Description: str
    Parameters: List[Parameter]
    ReturnValue: ReturnValue
    ExampleUse: str
    TestCases: List[TestCase]


ollama_model: str = "llama3.2"

my_prompt: str = """
You are an expert NodeJS export documentation writer. 
For each export you create a description, document parameters, document the return value, 
create and ExampleUse to be used as an example of the export, and some relevant TestCases that can 
be used to test the exports in a meaningful way. IMPORTANT make sure all code written for the ExampleUse and
TestCases compiles and is written as a js or jsx file.
Your job is to take the method immediately proceeding this sentence and 
use the codebase after it to create extensive documentation for that export.
"""


