# LLMarkdownDocs

This is a project to generate docs for the "@rescui/use-glow-hover" npm package.  

## TLDR

**If you're just looking for the best docs I was able to make look under examples/deepseek-r1:7b.md .**   
Despite not being the biggest model I used it had the best output

It can also technically be adapted for any npm package though I haven't tried that feel free to!   
Also, custom doc structures and any ollama model can be used with it!

If you have any install problems or questions feel free to email me at: azamolot@tcd.ie 

## Prerequisites 

[NodeJs v23.7.0](https://nodejs.org/en)  
[Ollama](https://ollama.com)  
[Python v3.11.9](https://www.python.org/downloads/release/python-3119/)  
[NPM v10.9.2](https://www.npmjs.com)

## Install

### Automatic Run

First install all python requirements
```bash
pip install -r code/requirements.txt
```
Next run the start script to install node packages 
```bash
chmod +x ./start.sh
./start.sh
```
### Manual Run

If you want to manually run this first install python requirements.

```bash
pip install -r code/requirements.txt
```

Then access the  code dirctory 
```bash
cd code
```
Pull the ollama model you want to use (make sure ollama is running)
```bash
ollama pull <model_to_use>
```
Install the node package
```bash
npm i <npm_package_to_install>
```
Run with parameters use "python3 main.py -h" if unsure
```bash
python3 main.py -p <npm_package_to_install> -e <space_seperated_exports> -m <model_to_use> -o <export_dir> -t <typescript_or_javascript>
```

This is whats done in the the start.sh script so feel free to look at that if you have any questions.


## How It Works

I wanted the generation of the docs to be automated and expandable to alternate packages.

I decided that because markdown is a very structured type of doccument just sending the codebase in and hoping it returns
a valid markdown file is useless.   
Instead I used ollama locally hosted models for a couple reasons:
1. Ollama allows structured outputs in the form of structured output.
2. Allows a wide variety of models to be used including potentially fine-tuned ones.
3. Whats the point of having an m-series macbook if you don't use the neural cores once in a while

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

## Examples and Thoughts
Under the examples directory you'll see the various models I've run through with typescript set to true as the typescript files
of the package had more to infer as they had an options class.  All the examples are raw outputs from the script apart from deepseek-r1:32b.md, 
which I made a small change as one of the code blocks didn't format right.  
The different models output wildly different things like in llama3.1:8b.md where in a description it links to a header that it
doesn't know exists and somehow that link works (line 22)!

The best I was able to create was deepseek-r1:7b.md it's quite extensive and you can consider it my submission.