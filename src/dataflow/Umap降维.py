from inspect import cleandoc
import pandas as pd

try:
    from cuml import UMAP as GPU_UMAP
    GPU_AVILABLE =True
except ImportError:
    import umap
    GPU_AVILABLE =False

class Umap:
    """
    使用UMAP算法对数据进行降维,支持GPU加速
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
                "近邻数量": ("INT", {
                    "default": 15,
                    "min": 2,
                    "max": 100,
                    "step": 1,
                    "tooltip": "n_neighbors:控制局部与全局结构平衡，较小值保留局部特征"
                }),
                "目标维度": ("INT", {
                    "default": 2,
                    "min": 2,
                    "max": 10,
                    "step": 1,
                    "tooltip": "n_components:降维后的维度"
                }),
            },
            "optional": {
                "最小距离": ("FLOAT", {
                    "default": 0.1,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "tooltip": "min_dist:低维空间中点的最小距离"
                }),
                "使用GPU":("BOOLEAN",{
                    "default":
                    GPU_AVAILABLE,
                    "tooltip":"使用GPU加速,需要安装cuml库"
                })
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("降维后数据帧",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "process"
    CATEGORY = "数学建模/数据预处理"

    def process(self, 数据帧, 近邻数量, 目标维度, 最小距离,使用GPU = GPU_AVILABLE):


        # 提取数值列进行降维
        numeric_df = 数据帧.select_dtypes(include=['number'])
        if numeric_df.empty:
            raise ValueError("数据帧中没有数值列可供降维")

        data = numeric_df.values

        if data.shape[1] < 2:
            raise ValueError("数据帧中数值列数量不足,无法进行降维")

        if 使用GPU:
            reducer = GPU_UMAP(
                n_neighbors=近邻数量,
                n_components=目标维度,
                min_dist=最小距离,
                random_state=42
            )
        else:
            reducer = umap.UMAP(
                n_neighbors=近邻数量,
                n_components=目标维度,
                min_dist=最小距离,
                random_state=42
            )

        # 执行降维
        embedding = reducer.fit_transform(numeric_df)

        # 转换为DataFrame返回
        result_df = pd.DataFrame(
            embedding, 
            columns=[f'UMAP_{i+1}' for i in range(目标维度)],
            index=数据帧.index
        )

        return (result_df,)

