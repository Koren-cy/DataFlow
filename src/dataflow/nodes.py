from .Example import *
from .ReadCSV import *
from .ShowAny import *
from .DropNA import *

# 一个包含所有要导出的节点及其名称的字典
# NOTE: 应使用全局唯一的名称
NODE_CLASS_MAPPINGS = {
    "Example": Example,
    "ReadCSV": ReadCSV,
    "ShowAny": ShowAny,
    "DropNA": DropNA,
}

# 一个包含节点人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example": "示例节点",
    "ReadCSV": "读取CSV文件",
    "ShowAny": "以文本显示",
    "DropNA": "删除含缺失值的行",
}
