from inspect import cleandoc
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler


class Normalize:
    """
    对数值列进行标准化处理
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
                "标准化方法": (["MinMax", "Standard", "Robust", "MaxAbs"], {
                    "default": "MinMax",
                    "tooltip": "MinMax: 缩放到[0,1]\nStandard: 标准化(z-score)\nRobust: 基于中位数和四分位数\nMaxAbs: 按最大绝对值缩放"
                }),
            },
            "optional": {
                "指定列": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "要标准化的列名，多个列名用逗号分隔。留空则处理所有数值列"
                }),
                "特征范围最小值": ("FLOAT", {
                    "default": 0.0,
                    "min": -10.0,
                    "max": 10.0,
                    "step": 0.1,
                    "tooltip": "仅用于MinMax方法，设置缩放后的最小值"
                }),
                "特征范围最大值": ("FLOAT", {
                    "default": 1.0,
                    "min": -10.0,
                    "max": 10.0,
                    "step": 0.1,
                    "tooltip": "仅用于MinMax方法，设置缩放后的最大值"
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("数据帧",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "normalize"

    CATEGORY = "数学建模/数据预处理"

    def normalize(self, 数据帧, 标准化方法="MinMax", 指定列="", 特征范围最小值=0.0, 特征范围最大值=1.0):
        # 复制数据帧以避免修改原始数据
        df = 数据帧.copy()
        
        # 确定要处理的列
        if 指定列.strip():
            # 用户指定了列
            target_cols = [col.strip() for col in 指定列.split(',') if col.strip()]
            # 检查列是否存在
            invalid_cols = [col for col in target_cols if col not in df.columns]
            if invalid_cols:
                raise ValueError(f"列名不存在: {invalid_cols}")
            # 检查列是否为数值类型
            non_numeric_cols = [col for col in target_cols if not pd.api.types.is_numeric_dtype(df[col])]
            if non_numeric_cols:
                raise ValueError(f"以下列不是数值类型，无法标准化: {non_numeric_cols}")
        else:
            # 自动选择所有数值列
            target_cols = df.select_dtypes(include=['number']).columns.tolist()
            if not target_cols:
                raise ValueError("数据帧中没有数值列可以进行标准化")
        
        # 检查是否有空值
        if df[target_cols].isnull().any().any():
            raise ValueError(f"目标列中存在缺失值，请先处理缺失值。含缺失值的列: {df[target_cols].columns[df[target_cols].isnull().any()].tolist()}")
        
        # 选择标准化方法
        if 标准化方法 == "MinMax":
            scaler = MinMaxScaler(feature_range=(特征范围最小值, 特征范围最大值))
        elif 标准化方法 == "Standard":
            scaler = StandardScaler()
        elif 标准化方法 == "Robust":
            scaler = RobustScaler()
        elif 标准化方法 == "MaxAbs":
            scaler = MaxAbsScaler()
        else:
            raise ValueError(f"不支持的标准化方法: {标准化方法}")
        
        # 执行标准化
        df[target_cols] = scaler.fit_transform(df[target_cols])
        
        return (df,)