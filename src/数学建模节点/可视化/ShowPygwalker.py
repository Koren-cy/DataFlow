from inspect import cleandoc
import pygwalker as pyg
import pandas as pd


class ShowPygwalker:
    """
    通过Pygwalker洞察数据
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "数据帧": ("DATAFRAME", {}),
            },
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = True


    def process(self, 数据帧=pd.DataFrame()):
        return {
            "ui": {
                "content": (pyg.to_html(数据帧),),
            }
        }