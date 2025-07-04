from inspect import cleandoc


class SelectColumns:
    """
    选择指定的列
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
                "列名": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "要选择的列名，多个列名用逗号分隔"
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("数据帧",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"

    CATEGORY = "数学建模/数据预处理"

    def process(self, 数据帧, 列名):
        if not 列名.strip():
            raise ValueError("请指定要选择的列名")
        
        # 解析列名
        column_names = [col.strip() for col in 列名.split(',') if col.strip()]
        
        # 检查列名是否存在
        invalid_cols = [col for col in column_names if col not in 数据帧.columns]
        if invalid_cols:
            raise ValueError(f"列名不存在: {invalid_cols}")
        
        return (数据帧[column_names],)