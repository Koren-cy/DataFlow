from comfy.comfy_types.node_typing import IO
from inspect import cleandoc
import json


class ShowAny:
    """
    将任意类型的数据装换成文本展示
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"source": (IO.ANY, {})},
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = True
    
    def process(self, source=None):
        value = 'None'
        if isinstance(source, str):
            value = source
        elif isinstance(source, (int, float, bool)):
            value = str(source)
        elif source is not None:
            try:
                value = json.dumps(source)
            except Exception:
                try:
                    value = str(source)
                except Exception:
                    value = 'source exists, but could not be serialized.'

        return {"ui": {"text": (value,)}}