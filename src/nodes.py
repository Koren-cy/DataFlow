from .Nodes.BalanceData import *
from .Nodes.DropINF import *
from .Nodes.DropNA import *
from .Nodes.Example import *
from .Nodes.Normalize import *
from .Nodes.PCA import *
from .Nodes.ReadCSV import *
from .Nodes.SelectColumns import *
from .Nodes.ShowAny import *
from .Nodes.ShowDOM import *
from .Nodes.ShowPygwalker import *
from .Nodes.ShowStreamlit import *
from .Nodes.UMAP import *

# 一个包含所有要导出的节点及其名称的字典
# NOTE: 应使用全局唯一的名称
NODE_CLASS_MAPPINGS = {
    "BalanceData": BalanceData,
    "DropINF": DropINF,
    "DropNA": DropNA,
    "Example": Example,
    "Normalize": Normalize,
    "PCA": PCA,
    "ReadCSV": ReadCSV,
    "SelectColumns": SelectColumns,
    "ShowAny": ShowAny,
    "ShowDOM": ShowDOM,
    "ShowPygwalker": ShowPygwalker,
    "ShowStreamlit": ShowStreamlit,
    "UMAP": Umap,
}

# 一个包含节点人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "BalanceData": "数据平衡",
    "DropINF": "删除含无穷值的行",
    "DropNA": "删除含缺失值的行",
    "Example": "示例节点",
    "Normalize": "数据标准化",
    "PCA": "PCA降维",
    "ReadCSV": "读取CSV文件",
    "SelectColumns": "选择指定列",
    "ShowAny": "以文本显示",
    "ShowDOM": "DOM容器",
    "ShowPygwalker": "Pygwalker容器",
    "ShowStreamlit": "Streamlit容器",
    "UMAP": "UMAP降维",
}
