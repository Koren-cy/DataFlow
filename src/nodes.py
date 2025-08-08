# from .Nodes.BalanceData import *
# from .Nodes.DropINF import *
# from .Nodes.DropNA import *
# from .Nodes.Example import *
# from .Nodes.Normalize import *
# from .Nodes.PCA import *
# from .Nodes.ReadCSV import *
# from .Nodes.SelectColumns import *
# from .Nodes.ShowAny import *
# from .Nodes.ShowDOM import *
# from .Nodes.ShowPygwalker import *
# from .Nodes.ShowStreamlit import *
# from .Nodes.UMAP import *

# 一个包含所有要导出的节点及其名称的字典
# NOTE: 应使用全局唯一的名称
NODE_CLASS_MAPPINGS = {
    # "BalanceData": BalanceData,
    # "DropINF": DropINF,
    # "DropNA": DropNA,
    # "Example": Example,
    # "Normalize": Normalize,
    # "PCA": PCA,
    # "ReadCSV": ReadCSV,
    # "SelectColumns": SelectColumns,
    # "ShowAny": ShowAny,
    # "ShowDOM": ShowDOM,
    # "ShowPygwalker": ShowPygwalker,
    # "ShowStreamlit": ShowStreamlit,
    # "UMAP": Umap,
}

# 一个包含节点人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    # "BalanceData": "数据平衡",
    # "DropINF": "删除含无穷值的行",
    # "DropNA": "删除含缺失值的行",
    # "Example": "示例节点",
    # "Normalize": "数据标准化",
    # "PCA": "PCA降维",
    # "ReadCSV": "读取CSV文件",
    # "SelectColumns": "选择指定列",
    # "ShowAny": "以文本显示",
    # "ShowDOM": "DOM容器",
    # "ShowPygwalker": "Pygwalker容器",
    # "ShowStreamlit": "Streamlit容器",
    # "UMAP": "UMAP降维",
}


def import_all_nodes(prefix:str, nodes_path:str, file_path:str):
    import os
    
    def is_python_file(path):
        return (os.path.isfile(path) 
                and os.path.splitext(path)[1] == '.py' 
                and not '__' in pathlib.Path(path).stem)
        
    def is_valid_dir(path):
        return (os.path.isdir(path) 
                and not '__' in pathlib.Path(path).stem)
    
    def import_nodes_from_dir(dir):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        for file in os.listdir(os.path.join(script_dir,dir[2:])):
            rel_path = os.path.join(dir,file)
            full_path = os.path.join(script_dir,rel_path[2:])
            
            if is_python_file(full_path):
                try:
                    module = importlib.import_module(
                        os.path.join(file_path,rel_path)
                        .replace('./','')
                        .replace('\\','.')
                        .replace('/','.')
                        .replace('.py',''))

                    category = '/'.join(
                        rel_path
                        .replace('./','')
                        .replace('\\','.')
                        .replace('/','.')
                        .replace('.py','')
                        .split('.')[:-1])
                    
                    for cls_name,cls in inspect.getmembers(module, inspect.isclass):
                        if cls_name != pathlib.Path(full_path).stem:
                            continue
                        
                        unique_name = f'{prefix}_{cls_name}'
                        
                        try:
                            full_doc = inspect.cleandoc(cls.__doc__)
                            simple_doc = full_doc.split('\n')[0]
                        except Exception as e:
                            full_doc = ''
                            simple_doc = ''
                            print(e)
                        
                        cls.CATEGORY = category
                        cls.DESCRIPTION = full_doc
                        cls.FUNCTION = 'process'
                        
                        NODE_CLASS_MAPPINGS[unique_name] = cls
                        NODE_DISPLAY_NAME_MAPPINGS[unique_name] = simple_doc
                        
                except Exception as e:
                    print(e)
                
            elif is_valid_dir(full_path):
                import_nodes_from_dir(rel_path)
            
    import importlib,pathlib,inspect
    import_nodes_from_dir(nodes_path)

import_all_nodes(prefix='DF', nodes_path='./数学建模节点', file_path='./custom_nodes/DataFlow/src')