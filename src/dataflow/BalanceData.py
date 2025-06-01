from inspect import cleandoc
import pandas as pd
import numpy as np
from collections import Counter


class BalanceData:
    """
    处理数据不平衡问题
    
    支持多种采样方法:
    - 随机过采样:对少数类进行随机重复采样
    - 随机欠采样:对多数类进行随机删除采样
    - SMOTE过采样:使用合成少数类过采样技术 (需要安装imbalanced-learn)
    - 组合采样:先过采样后欠采样
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
                "目标列": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "用于判断样本类别的目标列名"
                }),
                "采样方法": (["随机过采样", "随机欠采样", "SMOTE过采样", "组合采样"], {
                    "default": "随机过采样",
                    "tooltip": "随机过采样: 重复少数类样本\n随机欠采样: 删除多数类样本\nSMOTE过采样: 合成新的少数类样本\n组合采样: 先SMOTE过采样, 再随机欠采样"
                }),
            },
            "optional": {
                "采样策略": (["auto", "majority", "not minority", "not majority", "all"], {
                    "default": "auto",
                    "tooltip": "auto: 自动平衡到最大类的数量\nmajority: 只处理多数类\nnot minority: 处理除最少类外的所有类\nnot majority: 处理除最多类外的所有类\nall: 处理所有类"
                }),
                "随机种子": ("INT", {
                    "default": 42,
                    "min": 0,
                    "max": 9999,
                    "tooltip": "随机种子, 用于结果可重现"
                }),
                "k近邻数": ("INT", {
                    "default": 5,
                    "min": 1,
                    "max": 20,
                    "tooltip": "SMOTE算法中的k近邻数量"
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME", "STRING")
    RETURN_NAMES = ("数据帧", "采样信息")
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"

    CATEGORY = "数学建模/数据预处理"

    def process(self, 数据帧, 目标列, 采样方法="随机过采样", 采样策略="auto", 随机种子=42, k近邻数=5):
        if not 目标列.strip():
            raise ValueError("请指定目标列名")
        
        if 目标列 not in 数据帧.columns:
            raise ValueError(f"目标列 '{目标列}' 不存在")
        
        # 分离特征和目标
        X = 数据帧.drop(columns=[目标列])
        y = 数据帧[目标列]
        
        if 采样方法 == "随机过采样":
            X_resampled, y_resampled = self._random_oversample(X, y, 采样策略, 随机种子)
        elif 采样方法 == "随机欠采样":
            X_resampled, y_resampled = self._random_undersample(X, y, 采样策略, 随机种子)
        elif 采样方法 == "SMOTE过采样":
            X_resampled, y_resampled = self._smote_oversample(X, y, 采样策略, 随机种子, k近邻数)
        elif 采样方法 == "组合采样":
            X_resampled, y_resampled = self._combined_sampling(X, y, 采样策略, 随机种子, k近邻数)
        else:
            raise ValueError(f"不支持的采样方法: {采样方法}")
        
        return (pd.concat([X_resampled, y_resampled], axis=1), )
    
    def _random_oversample(self, X, y, strategy, random_state):
        """随机过采样"""
        np.random.seed(random_state)
        
        # 计算目标数量
        class_counts = Counter(y)
        if strategy == "auto":
            target_count = max(class_counts.values())
            target_counts = {cls: target_count for cls in class_counts.keys()}
        else:
            target_counts = class_counts
        
        X_resampled = []
        y_resampled = []
        
        for cls in class_counts.keys():
            cls_indices = y[y == cls].index
            cls_X = X.loc[cls_indices]
            cls_y = y.loc[cls_indices]
            
            current_count = len(cls_indices)
            target_count = target_counts.get(cls, current_count)
            
            if target_count > current_count:
                # 需要过采样
                additional_samples = target_count - current_count
                additional_indices = np.random.choice(cls_indices, additional_samples, replace=True)
                
                X_resampled.append(cls_X)
                X_resampled.append(X.loc[additional_indices])
                y_resampled.append(cls_y)
                y_resampled.append(y.loc[additional_indices])
            else:
                X_resampled.append(cls_X)
                y_resampled.append(cls_y)
        
        X_result = pd.concat(X_resampled, ignore_index=True)
        y_result = pd.concat(y_resampled, ignore_index=True)
        
        return X_result, y_result
    
    def _random_undersample(self, X, y, strategy, random_state):
        """随机欠采样"""
        np.random.seed(random_state)
        
        # 计算目标数量
        class_counts = Counter(y)
        if strategy == "auto":
            target_count = min(class_counts.values())
            target_counts = {cls: target_count for cls in class_counts.keys()}
        else:
            target_counts = class_counts
        
        X_resampled = []
        y_resampled = []
        
        for cls in class_counts.keys():
            cls_indices = y[y == cls].index
            cls_X = X.loc[cls_indices]
            cls_y = y.loc[cls_indices]
            
            current_count = len(cls_indices)
            target_count = target_counts.get(cls, current_count)
            
            if target_count < current_count:
                # 需要欠采样
                selected_indices = np.random.choice(cls_indices, target_count, replace=False)
                X_resampled.append(X.loc[selected_indices])
                y_resampled.append(y.loc[selected_indices])
            else:
                X_resampled.append(cls_X)
                y_resampled.append(cls_y)
        
        X_result = pd.concat(X_resampled, ignore_index=True)
        y_result = pd.concat(y_resampled, ignore_index=True)
        
        return X_result, y_result
    
    def _smote_oversample(self, X, y, strategy, random_state, k_neighbors):
        """SMOTE过采样"""
        try:
            from imblearn.over_sampling import SMOTE
        except ImportError:
            raise ImportError("SMOTE过采样需要安装 imbalanced-learn 库")
        
        # 确保所有特征都是数值型
        numeric_columns = X.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) != len(X.columns):
            raise ValueError("SMOTE算法要求所有特征都是数值型, 请先进行数据预处理")
        
        smote = SMOTE(sampling_strategy=strategy, random_state=random_state, k_neighbors=k_neighbors)
        X_resampled, y_resampled = smote.fit_resample(X, y)
        
        # 转换回DataFrame
        X_resampled = pd.DataFrame(X_resampled, columns=X.columns)
        y_resampled = pd.Series(y_resampled, name=y.name)
        
        return X_resampled, y_resampled
    
    def _combined_sampling(self, X, y, strategy, random_state, k_neighbors):
        """组合采样:先SMOTE过采样, 再随机欠采样"""
        try:
            from imblearn.combine import SMOTETomek
        except ImportError:
            raise ImportError("组合采样需要安装 imbalanced-learn 库")
        
        # 确保所有特征都是数值型
        numeric_columns = X.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) != len(X.columns):
            raise ValueError("组合采样算法要求所有特征都是数值型, 请先进行数据预处理")
        
        combined = SMOTETomek(sampling_strategy=strategy, random_state=random_state, 
                             smote=SMOTE(k_neighbors=k_neighbors, random_state=random_state))
        X_resampled, y_resampled = combined.fit_resample(X, y)
        
        # 转换回DataFrame
        X_resampled = pd.DataFrame(X_resampled, columns=X.columns)
        y_resampled = pd.Series(y_resampled, name=y.name)
        
        return X_resampled, y_resampled