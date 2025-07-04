from inspect import cleandoc


class DropNA:
    """
    删除含缺失值的行
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
            },
            "optional": {
                "子集": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "关注的列。\n指定列名，多个列名用逗号分隔。留空则检查所有列"
                }),
                "策略": (["any", "all"], {
                    "default": "any",
                    "tooltip": "any: 任一列有缺失值就删除该行\nall: 所有列都有缺失值才删除该行"
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("数据帧",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"

    CATEGORY = "数学建模/数据预处理"

    def process(self, 数据帧, 子集="", 策略="any"):
        subset_cols = None
        if 子集.strip():
            subset_cols = [col.strip() for col in 子集.split(',') if col.strip()]
            invalid_cols = [col for col in 子集 if col not in 数据帧.columns]
            if invalid_cols:
                raise ValueError(f"列名不存在: {invalid_cols}")
        
        return (数据帧.dropna(subset=subset_cols, how=策略),)