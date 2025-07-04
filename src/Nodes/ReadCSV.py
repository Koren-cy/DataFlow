from inspect import cleandoc
import pandas as pd


class ReadCSV:
    """
    读取CSV文件
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "文件路径": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("数据帧",)
    DESCRIPTION = cleandoc(__doc__ or "")
    FUNCTION = "process"

    CATEGORY = "数学建模/数据采集"

    def process(self, 文件路径):
        dataframe = pd.read_csv(文件路径.strip('\'\" '))
        return (dataframe,)