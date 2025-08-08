from inspect import cleandoc
import pygwalker as pyg
import pandas as pd


class ShowStreamlit:
    """
    通用的Streamlit可视化容器
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