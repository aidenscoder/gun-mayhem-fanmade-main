from typing import Literal

folders = Literal['src','.vscode','util','modules','util','root']
def folder(name:str,content:list[str]|tuple[str,...] = [],indent:str = ""):
    base = f"({name}):\n"  
    for i in content:
        base += indent+f"\t-{i}\n" 
    return base
        
class Folder:
    def __getitem__(self,name:folders|str):
        folder_name = name
        def wrapper(indent:int = 0,*content:str):
            indentation = ""
            for _ in range(indent):
                indentation += "\t"
            to_return = folder(folder_name,content,indentation)
            return to_return
        return wrapper
    
formater = Folder()
x = formater['root'](0,
    formater['.vscode'](1,
        'settings.json'
    ),
    formater['src'](1,
        formater['modules'](2,
            'drawing.py',
            'drawing.pyi'
        ),
        'main.py'
    ),
    formater['util'](1,
        'output #generated',
        'templater.py'
    )
)
with open('util\\output.txt','w') as file:
    file.write(x)