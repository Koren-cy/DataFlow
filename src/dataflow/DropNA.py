from inspect import cleandoc


class DropNA:
    """
    删除DataFrame中含缺失值的行
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
            },
            "optional": {
                "subset": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "指定列名，多个列名用逗号分隔。留空则检查所有列"
                }),
                "how": (["any", "all"], {
                    "default": "any",
                    "tooltip": "any: 任一列有缺失值就删除该行; all: 所有列都有缺失值才删除该行"
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("数据帧",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"

    CATEGORY = "数学建模/数据预处理"

    def process(self, dataframe, subset="", how="any"):
        # 处理subset参数
        subset_cols = None
        if subset.strip():
            subset_cols = [col.strip() for col in subset.split(',') if col.strip()]
            # 验证列名是否存在
            invalid_cols = [col for col in subset_cols if col not in dataframe.columns]
            if invalid_cols:
                raise ValueError(f"列名不存在: {invalid_cols}")
        
        # 删除含缺失值的行
        cleaned_df = dataframe.dropna(subset=subset_cols, how=how)
        
        return (cleaned_df,)