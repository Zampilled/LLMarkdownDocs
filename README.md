# LLMarkdownDocs

This is a project to generate docs for the "@rescui/use-glow-hover" npm package.

## Prerequisites 

Nodejs  
Ollama  
Python3 

## Install

### Automatic Run
```bash
pip install -r code/requirements.txt
```

```bash
chmod +x ./start.sh
./start.sh
```
### Manual Run


## How It Works

I wanted the generation of the docs to be automated and expandable to alternate packages.

I decided that because markdown is a very structured type of doccument just sending the codebase in and hoping it returns
a valid markdown file is useless.   
Instead I used ollama locally hosted models for a couple reasons:
1. Ollama allows structured outputs in the form of structured output.
2. Can be dockerized to make a completely independent system.
3. Whats the point of having an m-series macbook if you don't use it once in a while

### The Process

#### Input
To get it to work we first input a package, its exports, a ollama model to use, and the markdown out filename.

#### Package Files

First the package files is extracted in code/llm_processing/getFiles.py .  
This is to give our model context when processing prompts. 

####  LLM Response

For each export we need to give it our prompt with the name of the export and the codebase.  
This prompt is defined in config.py .  
To get useful outputs from the model I use structured outputs where we can define a class structure and the output will match it.  
The current structure I use is as follows:  
```python
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
```
This along with the prompt returns an dict structured as these classes.  

#### Processing Dict to Markdown
The next part is to process this dict into valid markdown.  
This can be done recursively where each key in an object gets a heading of lower importance than its parent.  
This means that this class structure can be changed to whatever type of doccumentation is best suited for a package and 
the markdown processing code doesn't need to change.  
This code can be found under code/llm_processing/createMarkdown.py

## Issues