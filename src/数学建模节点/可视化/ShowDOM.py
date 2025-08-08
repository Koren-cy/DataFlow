from comfy.comfy_types.node_typing import IO
from inspect import cleandoc
import pandas as pd
import json


class ShowDOM:
    """
    通用的html可视化容器
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "x": ("DATAFRAME", {}),
                "y": ("DATAFRAME", {}),
                "data": (IO.ANY, {}),
            },
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = True
    
    def process(self, x=pd.DataFrame(),y=pd.DataFrame(),data=None):
        value = ''
        if isinstance(data, str):
            value = data
        elif isinstance(data, (int, float, bool)):
            value = str(data)
        elif data is not None:
            try:
                value = json.dumps(data)
            except Exception:
                try:
                    value = str(data)
                except Exception:
                    value = 'data exists, but could not be serialized.'
        return {
            "ui": {
                "x": ("" if x.empty else x.to_json(orient="columns"),),
                "y": ("" if y.empty else y.to_json(orient="columns"),),
                "data": (value,),
            }
        }
        