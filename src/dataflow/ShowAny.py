from inspect import cleandoc


import json
from comfy.comfy_types.node_typing import IO


class ShowAny:
    """
    将任意类型的数据装换成文本展示
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"source": (IO.ANY, {})},
        }

    RETURN_TYPES = ()
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"
    OUTPUT_NODE = True

    CATEGORY = "数学建模/可视化"

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