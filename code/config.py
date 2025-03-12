from typing import List

from pydantic import BaseModel


"""
LLM response structure
This is the structure to be used to dictate how the markdown file is generated.
Fields are inferred through the name and type of the field.
Any field named "Name" will be replaced in the markdown with its value.
Any field named "Code" or "ExampleUse" will be surrounded by a code block in the markdown.
"""
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

"""
----------------------------------------------------
"""

#The prompt to be used by the model
my_prompt: str = """
You are an expert NodeJS export documentation writer. 
For each export you create a description, document parameters, document the return value, 
create and ExampleUse to be used as an example of the export, and some relevant TestCases that can 
be used to test.sh the exports in a meaningful way. IMPORTANT make sure all code written for the ExampleUse and
TestCases compiles and is written as a valid code that is well formated.
Your job is to take the method immediately proceeding this sentence and 
use the codebase after it to create extensive documentation for that export.
"""


