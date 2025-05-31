from inspect import cleandoc
import pandas as pd


class ReadCSV:
    """
    读取CSV文件
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("DataFrame",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"

    CATEGORY = "数学建模/数据采集"

    def process(self, file_path):
        df = pd.read_csv(file_path)
        return (df,)