def folder(name:str,content:list[str] = []):
    base = f"{name}:\n"  
    for i in content:
        base += f"\t-{i}\n" 
    return base
        
class Pack:
    def __class_getitem__(cls,name:str):
        def wrapper(content:list[str] = []):
            return folder(name,content)
        return wrapper
    
