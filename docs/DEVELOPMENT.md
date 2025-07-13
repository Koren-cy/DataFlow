# DataFlow 开发者指南

欢迎参与DataFlow项目的开发！本指南将帮助您了解项目结构、开发流程和最佳实践。

## 目录

- [开发环境设置](#开发环境设置)
- [项目结构](#项目结构)
- [开发流程](#开发流程)
- [代码规范](#代码规范)
- [测试指南](#测试指南)
- [文档编写](#文档编写)
- [发布流程](#发布流程)

## 开发环境设置

### 系统要求

- **操作系统**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.8 或更高版本
- **内存**: 8GB RAM (推荐 16GB+)
- **存储**: 2GB 可用空间

### 环境配置

#### 1. 克隆仓库

```bash
git clone https://github.com/Koren-cy/DataFlow.git
cd DataFlow
```

#### 2. 创建虚拟环境

```bash
# 使用 venv
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

#### 3. 安装依赖

```bash
# 安装开发依赖
pip install -e .[dev]

# 安装 pre-commit 钩子
pre-commit install
```

#### 4. 验证安装

```bash
# 运行测试
pytest

# 检查代码格式
ruff check src/

# 类型检查
mypy src/
```

### IDE 配置

#### VS Code 推荐设置

创建 `.vscode/settings.json`：

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "ruff",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

#### 推荐扩展

- Python
- Pylance
- Python Test Explorer
- GitLens
- Markdown All in One

---

## 项目结构

```
DataFlow/
├── src/                    # 源代码目录
│   ├── Helper/            # 辅助工具模块
│   │   └── visualization.py
│   ├── Nodes/             # 节点实现
│   │   ├── __init__.py
│   │   ├── BalanceData.py
│   │   ├── DropINF.py
│   │   ├── DropNA.py
│   │   ├── Example.py
│   │   ├── Normalize.py
│   │   ├── PCA.py
│   │   ├── ReadCSV.py
│   │   ├── SelectColumns.py
│   │   ├── ShowAny.py
│   │   ├── ShowDOM.py
│   │   ├── ShowPygwalker.py
│   │   ├── ShowStreamlit.py
│   │   └── UMAP.py
│   └── nodes.py           # 节点注册
├── web/                   # Web 资源
│   └── Nodes/
├── tests/                 # 测试文件
├── docs/                  # 文档
├── doc/                   # 图片资源
├── pyproject.toml         # 项目配置
├── README.md              # 项目说明
├── LICENSE                # 许可证
└── .gitignore            # Git 忽略文件
```

### 核心模块说明

#### `src/nodes.py`

节点注册中心，包含：

- `NODE_CLASS_MAPPINGS`: 节点类映射
- `NODE_DISPLAY_NAME_MAPPINGS`: 节点显示名称映射

#### `src/Nodes/`

所有节点的实现目录，每个节点文件应包含：

- 节点类定义
- `INPUT_TYPES` 类方法
- `RETURN_TYPES` 和 `RETURN_NAMES`
- `FUNCTION` 和 `CATEGORY`
- 主要处理函数

#### `src/Helper/`

辅助工具模块，包含：

- 可视化工具
- 数据处理工具
- 通用工具函数

---

## 开发流程

### Git 工作流

我们使用 **Git Flow** 工作流：

```
main (生产分支)
├── develop (开发分支)
│   ├── feature/new-node (功能分支)
│   ├── feature/improve-ui (功能分支)
│   └── hotfix/critical-bug (热修复分支)
└── release/v0.1.0 (发布分支)
```

### 分支命名规范

- **功能分支**: `feature/功能描述`
- **修复分支**: `bugfix/问题描述`
- **热修复**: `hotfix/紧急修复`
- **发布分支**: `release/版本号`

### 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<类型>[可选范围]: <描述>

[可选正文]

[可选脚注]
```

#### 类型说明

- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

#### 示例

```bash
git commit -m "feat(nodes): 添加新的数据平衡节点"
git commit -m "fix(pca): 修复维度检查逻辑错误"
git commit -m "docs: 更新API文档"
```

---

## 代码规范

### Python 代码规范

#### 1. 代码格式

使用 `ruff` 进行代码格式化：

```bash
# 格式化代码
ruff format src/

# 检查代码
ruff check src/
```

#### 2. 类型注解

所有公共函数必须包含类型注解：

```python
from typing import Optional, Tuple, Dict, Any
import pandas as pd

def process_data(
    dataframe: pd.DataFrame,
    columns: Optional[str] = None,
    normalize: bool = True
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """处理数据的示例函数。
    
    Args:
        dataframe: 输入的数据框
        columns: 可选的列名列表
        normalize: 是否进行标准化
        
    Returns:
        处理后的数据框和元数据字典
        
    Raises:
        ValueError: 当输入数据无效时
    """
    # 实现代码
    pass
```

#### 3. 文档字符串

使用 Google 风格的文档字符串：

```python
class ExampleNode:
    """
    示例节点的详细描述。
    
    这个节点用于演示如何编写标准的ComfyUI节点。
    支持多种输入类型和参数配置。
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """定义节点的输入类型。
        
        Returns:
            包含输入类型定义的字典
        """
        return {
            "required": {
                "input_data": ("DATAFRAME", {}),
            },
            "optional": {
                "parameter": ("STRING", {"default": ""}),
            }
        }
```

#### 4. 错误处理

使用明确的异常类型和错误信息：

```python
def validate_input(dataframe: pd.DataFrame, columns: str) -> None:
    """验证输入参数。"""
    if dataframe.empty:
        raise ValueError("输入数据框不能为空")
    
    if columns:
        col_list = [col.strip() for col in columns.split(',')]
        missing_cols = [col for col in col_list if col not in dataframe.columns]
        if missing_cols:
            raise KeyError(f"以下列不存在: {missing_cols}")
```

### 节点开发规范

#### 1. 节点类结构

```python
from inspect import cleandoc
import pandas as pd
from typing import Tuple, Optional

class NewNode:
    """
    节点功能的详细描述。
    
    包括使用场景、算法原理、注意事项等。
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # 必需参数
            },
            "optional": {
                # 可选参数
            }
        }
    
    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("输出数据",)
    DESCRIPTION = cleandoc(__doc__ or "")
    FUNCTION = "process"
    CATEGORY = "数学建模/分类名称"
    
    def process(self, **kwargs) -> Tuple[pd.DataFrame]:
        """主要处理函数。"""
        # 实现逻辑
        pass
```

#### 2. 参数定义规范

```python
@classmethod
def INPUT_TYPES(cls):
    return {
        "required": {
            "数据帧": ("DATAFRAME", {}),
            "目标维度": ("INT", {
                "default": 2,
                "min": 1,
                "max": 100,
                "step": 1,
                "tooltip": "降维后的维度数"
            }),
            "方法选择": (["方法1", "方法2", "方法3"], {
                "default": "方法1",
                "tooltip": "选择处理方法"
            }),
        },
        "optional": {
            "指定列": ("STRING", {
                "multiline": False,
                "default": "",
                "tooltip": "要处理的列名，逗号分隔"
            }),
        }
    }
```

#### 3. 节点注册

在 `src/nodes.py` 中注册新节点：

```python
# 导入新节点
from .Nodes.NewNode import *

# 添加到映射字典
NODE_CLASS_MAPPINGS = {
    # 现有节点...
    "NewNode": NewNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # 现有节点...
    "NewNode": "新节点显示名称",
}
```

---

## 测试指南

### 测试结构

```
tests/
├── __init__.py
├── conftest.py           # 测试配置和fixtures
├── test_nodes.py         # 节点测试
├── test_helpers.py       # 辅助函数测试
├── data/                 # 测试数据
│   ├── sample.csv
│   └── test_data.json
└── fixtures/             # 测试fixtures
    └── sample_dataframes.py
```

### 编写测试

#### 1. 节点测试示例

```python
import pytest
import pandas as pd
import numpy as np
from src.Nodes.PCA import PCA

class TestPCANode:
    """PCA节点测试类。"""
    
    @pytest.fixture
    def sample_data(self):
        """创建测试数据。"""
        np.random.seed(42)
        data = np.random.randn(100, 5)
        return pd.DataFrame(data, columns=[f'feature_{i}' for i in range(5)])
    
    @pytest.fixture
    def pca_node(self):
        """创建PCA节点实例。"""
        return PCA()
    
    def test_basic_pca(self, pca_node, sample_data):
        """测试基本PCA功能。"""
        result = pca_node.process(
            数据帧=sample_data,
            目标维度=2,
            可视化类型="散点图"
        )
        
        assert len(result) == 1
        assert isinstance(result[0], pd.DataFrame)
        assert result[0].shape[1] == 2
        assert result[0].shape[0] == sample_data.shape[0]
    
    def test_invalid_dimensions(self, pca_node, sample_data):
        """测试无效维度参数。"""
        with pytest.raises(ValueError, match="目标维度.*必须小于特征数量"):
            pca_node.process(
                数据帧=sample_data,
                目标维度=10,  # 超过特征数量
                可视化类型="散点图"
            )
    
    def test_missing_values(self, pca_node):
        """测试包含缺失值的数据。"""
        data_with_nan = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [1, 2, 3, 4],
            'C': [1, 2, 3, 4]
        })
        
        with pytest.raises(ValueError, match="目标列中存在缺失值"):
            pca_node.process(
                数据帧=data_with_nan,
                目标维度=2,
                可视化类型="散点图"
            )
```

#### 2. 参数化测试

```python
@pytest.mark.parametrize("dimensions,expected_shape", [
    (2, (100, 2)),
    (3, (100, 3)),
    (4, (100, 4)),
])
def test_different_dimensions(self, pca_node, sample_data, dimensions, expected_shape):
    """测试不同的降维维度。"""
    result = pca_node.process(
        数据帧=sample_data,
        目标维度=dimensions,
        可视化类型="散点图"
    )
    
    assert result[0].shape == expected_shape
```

#### 3. 性能测试

```python
import time

def test_performance_large_dataset(self, pca_node):
    """测试大数据集的性能。"""
    # 创建大数据集
    large_data = pd.DataFrame(
        np.random.randn(10000, 50),
        columns=[f'feature_{i}' for i in range(50)]
    )
    
    start_time = time.time()
    result = pca_node.process(
        数据帧=large_data,
        目标维度=2,
        可视化类型="散点图"
    )
    end_time = time.time()
    
    # 确保在合理时间内完成
    assert end_time - start_time < 10  # 10秒内完成
    assert result[0].shape == (10000, 2)
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_nodes.py

# 运行特定测试类
pytest tests/test_nodes.py::TestPCANode

# 运行特定测试方法
pytest tests/test_nodes.py::TestPCANode::test_basic_pca

# 生成覆盖率报告
pytest --cov=src --cov-report=html

# 详细输出
pytest -v

# 并行运行测试
pytest -n auto
```

---

## 文档编写

### 文档类型

1. **API文档**: 详细的接口说明
2. **用户指南**: 面向最终用户的使用说明
3. **开发者指南**: 面向开发者的技术文档
4. **示例教程**: 具体的使用案例

### Markdown 规范

#### 1. 文档结构

```markdown
# 文档标题

简短的文档描述。

## 目录

- [章节1](#章节1)
- [章节2](#章节2)

## 章节1

### 子章节1.1

内容...

### 子章节1.2

内容...

## 章节2

内容...

---

*最后更新: 日期*
```

#### 2. 代码块

```markdown
# Python代码
```python
def example_function():
    return "Hello, World!"
```

# Bash命令
```bash
pip install dataflow
```

# JSON配置
```json
{
    "key": "value"
}
```
```

#### 3. 表格

```markdown
| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 值1 | 值2 | 值3 |
| 值4 | 值5 | 值6 |
```

#### 4. 链接和引用

```markdown
# 外部链接
[链接文本](https://example.com)

# 内部链接
[章节标题](#章节标题)

# 图片
![图片描述](path/to/image.png)

# 引用
> 这是一个引用块
```

---

## 发布流程

### 版本号规范

使用 [语义化版本](https://semver.org/lang/zh-CN/) (SemVer)：

- **主版本号**: 不兼容的API修改
- **次版本号**: 向下兼容的功能性新增
- **修订号**: 向下兼容的问题修正

示例: `1.2.3`

### 发布步骤

#### 1. 准备发布

```bash
# 确保在develop分支
git checkout develop
git pull origin develop

# 运行所有测试
pytest

# 检查代码质量
ruff check src/
mypy src/
```

#### 2. 创建发布分支

```bash
# 创建发布分支
git checkout -b release/v1.0.0

# 更新版本号
bump-my-version bump minor  # 或 major/patch

# 更新CHANGELOG
# 编辑 CHANGELOG.md

# 提交更改
git add .
git commit -m "chore: 准备发布 v1.0.0"
```

#### 3. 合并到主分支

```bash
# 合并到main
git checkout main
git merge release/v1.0.0
git tag v1.0.0
git push origin main --tags

# 合并回develop
git checkout develop
git merge release/v1.0.0
git push origin develop

# 删除发布分支
git branch -d release/v1.0.0
```

#### 4. GitHub发布

1. 在GitHub上创建新的Release
2. 选择刚创建的tag
3. 填写发布说明
4. 发布

#### 5. 发布到PyPI

```bash
# 构建包
python -m build

# 检查包
twine check dist/*

# 上传到PyPI
twine upload dist/*
```

---

## 最佳实践

### 代码质量

1. **单一职责**: 每个函数只做一件事
2. **可读性**: 代码应该自解释
3. **可测试性**: 编写易于测试的代码
4. **性能**: 考虑算法复杂度和内存使用

### 协作开发

1. **小步提交**: 频繁提交小的更改
2. **清晰描述**: 提交信息要清晰明确
3. **代码审查**: 所有PR都需要代码审查
4. **文档同步**: 代码更改时同步更新文档

### 问题解决

1. **日志记录**: 添加适当的日志信息
2. **错误处理**: 优雅地处理异常情况
3. **用户反馈**: 提供有用的错误信息
4. **性能监控**: 监控关键操作的性能

---

## 常见问题

### Q: 如何添加新的依赖？

A: 在 `pyproject.toml` 的 `dependencies` 部分添加新依赖，然后运行 `pip install -e .`。

### Q: 如何处理大数据集？

A: 考虑使用分块处理、内存映射或采样技术。确保在文档中说明内存要求。

### Q: 如何调试节点？

A: 使用 `ShowAny` 节点查看中间结果，或在代码中添加 `print` 语句。

### Q: 如何优化性能？

A: 使用性能分析工具（如 `cProfile`），优化算法复杂度，考虑并行处理。

---

## 联系方式

- **项目维护者**: Koren
- **邮箱**: koren.cai.cy@gmail.com
- **GitHub**: [DataFlow Issues](https://github.com/Koren-cy/DataFlow/issues)

---

*本文档持续更新中，如有问题请提交Issue或PR。*