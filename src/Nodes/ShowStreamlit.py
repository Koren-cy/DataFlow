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
    DESCRIPTION = cleandoc(__doc__ or "")
    FUNCTION = "process"
    OUTPUT_NODE = True

    CATEGORY = "数学建模/可视化"

    def process(self, 数据帧=pd.DataFrame()):
        return {
            "ui": {
                "content": (pyg.to_html(数据帧),),
            }
        }