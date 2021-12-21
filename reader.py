import os
import ast

def tryeval(val):
  try:
    val = ast.literal_eval(val)
  except ValueError:
    pass
  return val

def Reader(file_name: str, div:str = ":", _t:bool = False) -> dict:
    loader_content = None

    configs = {}

    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, file_name)

    with open(filepath , "r") as loader:
        loader_content = loader.read()

    # read through each line of the loader
    for line in loader_content.split("\n"):
        if line != "":
            value = tryeval(line.split(div)[1].strip())
    
            configs.update({line.split(div)[0].strip(): f"{value}" if not _t else f"{value}: {type(value)}"})

    return configs