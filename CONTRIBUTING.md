# 贡献指南

感谢您对DataFlow项目的关注！我们欢迎并感激任何形式的贡献，无论是代码、文档、bug报告还是功能建议。

## 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发环境设置](#开发环境设置)
- [提交指南](#提交指南)
- [代码规范](#代码规范)
- [测试要求](#测试要求)
- [文档贡献](#文档贡献)
- [问题报告](#问题报告)
- [功能请求](#功能请求)
- [Pull Request流程](#pull-request流程)
- [社区支持](#社区支持)

## 行为准则

### 我们的承诺

为了营造一个开放和友好的环境，我们作为贡献者和维护者承诺，无论年龄、体型、残疾、种族、性别认同和表达、经验水平、国籍、个人形象、种族、宗教或性取向如何，参与我们项目和社区的每个人都能享受无骚扰的体验。

### 我们的标准

有助于创造积极环境的行为包括：

- 使用友好和包容的语言
- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

不可接受的行为包括：

- 使用性化的语言或图像，以及不受欢迎的性关注或性骚扰
- 恶意评论、侮辱/贬损评论，以及个人或政治攻击
- 公开或私下骚扰
- 未经明确许可发布他人的私人信息，如物理地址或电子地址
- 在专业环境中可能被合理认为不适当的其他行为

### 执行

如果您遇到不当行为，请联系项目团队：koren.cai.cy@gmail.com

---

## 如何贡献

### 贡献类型

我们欢迎以下类型的贡献：

#### 🐛 Bug修复
- 修复现有功能中的错误
- 改进错误处理
- 性能问题修复

#### ✨ 新功能
- 新的数据处理节点
- 新的机器学习算法
- 新的可视化组件
- API扩展

#### 📚 文档改进
- API文档完善
- 使用教程编写
- 代码注释改进
- 翻译工作

#### 🎨 用户体验优化
- 界面改进
- 交互优化
- 错误信息改进
- 性能优化

#### 🧪 测试
- 单元测试编写
- 集成测试
- 性能测试
- 边界条件测试

### 贡献流程概览

1. **Fork项目** - 创建项目的个人副本
2. **创建分支** - 为您的更改创建功能分支
3. **开发** - 实现您的更改
4. **测试** - 确保所有测试通过
5. **提交** - 遵循提交信息规范
6. **Push** - 推送到您的Fork
7. **Pull Request** - 创建PR并等待审查

---

## 开发环境设置

### 系统要求

- **Python**: 3.8 或更高版本
- **Git**: 最新版本
- **操作系统**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **内存**: 8GB RAM (推荐 16GB+)

### 快速设置

```bash
# 1. Fork并克隆仓库
git clone https://github.com/YOUR_USERNAME/DataFlow.git
cd DataFlow

# 2. 添加上游仓库
git remote add upstream https://github.com/Koren-cy/DataFlow.git

# 3. 创建虚拟环境
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 4. 安装开发依赖
pip install -e .[dev]

# 5. 安装pre-commit钩子
pre-commit install

# 6. 验证安装
pytest
ruff check src/
mypy src/
```

### IDE配置

#### VS Code推荐设置

创建 `.vscode/settings.json`：

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "ruff",
    "python.testing.pytestEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        ".mypy_cache": true,
        ".pytest_cache": true
    }
}
```

#### 推荐扩展

- Python
- Pylance
- Python Test Explorer
- GitLens
- Markdown All in One
- Better Comments

---

## 提交指南

### 分支策略

我们使用Git Flow工作流：

```
main (生产分支)
├── develop (开发分支)
│   ├── feature/功能名称 (功能分支)
│   ├── bugfix/问题描述 (修复分支)
│   └── hotfix/紧急修复 (热修复分支)
└── release/版本号 (发布分支)
```

### 分支命名规范

- **功能分支**: `feature/add-excel-reader`
- **修复分支**: `bugfix/fix-memory-leak`
- **热修复**: `hotfix/critical-security-fix`
- **文档**: `docs/update-api-guide`
- **测试**: `test/add-pca-tests`

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
- `style`: 代码格式调整（不影响功能）
- `refactor`: 代码重构（不是新功能也不是修复bug）
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动
- `ci`: CI/CD相关
- `build`: 构建系统或外部依赖变动

#### 提交信息示例

```bash
# 好的提交信息
git commit -m "feat(nodes): 添加Excel文件读取节点"
git commit -m "fix(pca): 修复大数据集内存溢出问题"
git commit -m "docs: 更新API文档中的参数说明"
git commit -m "test: 添加UMAP节点的单元测试"

# 包含正文的提交
git commit -m "feat(visualization): 添加交互式3D散点图

- 支持鼠标旋转和缩放
- 添加颜色映射选项
- 优化大数据集渲染性能

Closes #123"

# 破坏性变更
git commit -m "feat!: 重构节点接口以支持异步处理

BREAKING CHANGE: 所有节点的process方法现在返回Promise"
```

### 提交最佳实践

1. **原子性提交**: 每个提交只包含一个逻辑变更
2. **频繁提交**: 小步快跑，避免大型提交
3. **清晰描述**: 提交信息要清楚说明做了什么和为什么
4. **测试通过**: 提交前确保所有测试通过
5. **代码格式**: 使用pre-commit钩子自动格式化

---

## 代码规范

### Python代码风格

我们使用以下工具确保代码质量：

- **ruff**: 代码格式化和静态检查
- **mypy**: 类型检查
- **pytest**: 测试框架

#### 代码格式化

```bash
# 格式化代码
ruff format src/

# 检查代码风格
ruff check src/

# 自动修复可修复的问题
ruff check src/ --fix
```

#### 类型注解

所有公共函数必须包含类型注解：

```python
from typing import Optional, Tuple, Dict, Any, List
import pandas as pd

def process_dataframe(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    normalize: bool = True
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """处理DataFrame的示例函数。
    
    Args:
        df: 输入的DataFrame
        columns: 要处理的列名列表，None表示处理所有列
        normalize: 是否进行标准化处理
        
    Returns:
        处理后的DataFrame和元数据字典
        
    Raises:
        ValueError: 当输入数据无效时
        KeyError: 当指定的列不存在时
    """
    # 实现代码
    pass
```

#### 文档字符串

使用Google风格的文档字符串：

```python
class DataProcessor:
    """数据处理器类。
    
    这个类提供了各种数据处理功能，包括清洗、转换和分析。
    
    Attributes:
        config: 处理器配置字典
        logger: 日志记录器实例
        
    Example:
        >>> processor = DataProcessor({"normalize": True})
        >>> result = processor.process(dataframe)
    """
    
    def __init__(self, config: Dict[str, Any]) -> None:
        """初始化数据处理器。
        
        Args:
            config: 配置字典，包含处理参数
            
        Raises:
            ValueError: 当配置无效时
        """
        pass
```

#### 错误处理

使用明确的异常类型和有用的错误信息：

```python
def validate_dataframe(df: pd.DataFrame, required_columns: List[str]) -> None:
    """验证DataFrame的有效性。"""
    if df.empty:
        raise ValueError("DataFrame不能为空")
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise KeyError(f"缺少必需的列: {missing_columns}")
    
    if df.isnull().any().any():
        null_columns = df.columns[df.isnull().any()].tolist()
        raise ValueError(f"以下列包含缺失值: {null_columns}")
```

### 节点开发规范

#### 节点类结构

```python
from inspect import cleandoc
from typing import Tuple, Optional, Dict, Any
import pandas as pd

class NewDataNode:
    """
    新数据处理节点。
    
    详细描述节点的功能、使用场景和注意事项。
    包括算法原理、参数说明和示例用法。
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """定义节点的输入类型。
        
        Returns:
            包含输入类型定义的字典
        """
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
                "处理方法": (["方法1", "方法2", "方法3"], {
                    "default": "方法1",
                    "tooltip": "选择数据处理方法"
                }),
            },
            "optional": {
                "参数值": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.1,
                    "tooltip": "处理参数的数值"
                }),
            }
        }
    
    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("处理结果",)
    DESCRIPTION = cleandoc(__doc__ or "")
    FUNCTION = "process"
    CATEGORY = "数学建模/数据处理"
    
    def process(
        self,
        数据帧: pd.DataFrame,
        处理方法: str,
        参数值: float = 1.0
    ) -> Tuple[pd.DataFrame]:
        """执行数据处理。
        
        Args:
            数据帧: 输入的数据
            处理方法: 选择的处理方法
            参数值: 处理参数
            
        Returns:
            处理后的数据元组
            
        Raises:
            ValueError: 当输入参数无效时
        """
        # 参数验证
        self._validate_inputs(数据帧, 处理方法, 参数值)
        
        # 执行处理
        result = self._execute_processing(数据帧, 处理方法, 参数值)
        
        return (result,)
    
    def _validate_inputs(
        self,
        df: pd.DataFrame,
        method: str,
        param: float
    ) -> None:
        """验证输入参数。"""
        if df.empty:
            raise ValueError("输入数据不能为空")
        
        valid_methods = ["方法1", "方法2", "方法3"]
        if method not in valid_methods:
            raise ValueError(f"无效的处理方法: {method}")
        
        if not 0.0 <= param <= 10.0:
            raise ValueError(f"参数值必须在0.0-10.0范围内: {param}")
    
    def _execute_processing(
        self,
        df: pd.DataFrame,
        method: str,
        param: float
    ) -> pd.DataFrame:
        """执行具体的处理逻辑。"""
        # 实现处理逻辑
        result = df.copy()
        # ... 处理代码 ...
        return result
```

#### 节点注册

在 `src/nodes.py` 中注册新节点：

```python
# 导入新节点
from .Nodes.NewDataNode import NewDataNode

# 添加到映射字典
NODE_CLASS_MAPPINGS = {
    # ... 现有节点 ...
    "NewDataNode": NewDataNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # ... 现有节点 ...
    "NewDataNode": "新数据处理节点",
}
```

---

## 测试要求

### 测试结构

```
tests/
├── __init__.py
├── conftest.py              # 测试配置和fixtures
├── test_nodes/              # 节点测试
│   ├── __init__.py
│   ├── test_data_nodes.py   # 数据处理节点测试
│   ├── test_ml_nodes.py     # 机器学习节点测试
│   └── test_viz_nodes.py    # 可视化节点测试
├── test_helpers/            # 辅助函数测试
│   ├── __init__.py
│   └── test_visualization.py
├── data/                    # 测试数据
│   ├── sample.csv
│   ├── test_data.json
│   └── large_dataset.csv
└── fixtures/                # 测试fixtures
    ├── __init__.py
    └── sample_dataframes.py
```

### 编写测试

#### 基本测试模板

```python
import pytest
import pandas as pd
import numpy as np
from src.Nodes.NewDataNode import NewDataNode

class TestNewDataNode:
    """新数据节点测试类。"""
    
    @pytest.fixture
    def sample_data(self) -> pd.DataFrame:
        """创建测试数据。"""
        np.random.seed(42)
        return pd.DataFrame({
            'A': np.random.randn(100),
            'B': np.random.randn(100),
            'C': np.random.randint(0, 3, 100),
            'D': np.random.choice(['X', 'Y', 'Z'], 100)
        })
    
    @pytest.fixture
    def node(self) -> NewDataNode:
        """创建节点实例。"""
        return NewDataNode()
    
    def test_basic_functionality(self, node, sample_data):
        """测试基本功能。"""
        result = node.process(
            数据帧=sample_data,
            处理方法="方法1",
            参数值=1.0
        )
        
        assert len(result) == 1
        assert isinstance(result[0], pd.DataFrame)
        assert not result[0].empty
    
    def test_input_validation(self, node):
        """测试输入验证。"""
        empty_df = pd.DataFrame()
        
        with pytest.raises(ValueError, match="输入数据不能为空"):
            node.process(
                数据帧=empty_df,
                处理方法="方法1",
                参数值=1.0
            )
    
    def test_invalid_method(self, node, sample_data):
        """测试无效方法参数。"""
        with pytest.raises(ValueError, match="无效的处理方法"):
            node.process(
                数据帧=sample_data,
                处理方法="无效方法",
                参数值=1.0
            )
    
    def test_parameter_bounds(self, node, sample_data):
        """测试参数边界。"""
        with pytest.raises(ValueError, match="参数值必须在0.0-10.0范围内"):
            node.process(
                数据帧=sample_data,
                处理方法="方法1",
                参数值=-1.0
            )
    
    @pytest.mark.parametrize("method,expected_behavior", [
        ("方法1", "behavior1"),
        ("方法2", "behavior2"),
        ("方法3", "behavior3"),
    ])
    def test_different_methods(self, node, sample_data, method, expected_behavior):
        """测试不同的处理方法。"""
        result = node.process(
            数据帧=sample_data,
            处理方法=method,
            参数值=1.0
        )
        
        # 根据expected_behavior验证结果
        assert len(result) == 1
        # 添加具体的验证逻辑
    
    def test_performance_large_dataset(self, node):
        """测试大数据集性能。"""
        large_data = pd.DataFrame({
            'A': np.random.randn(10000),
            'B': np.random.randn(10000),
        })
        
        import time
        start_time = time.time()
        
        result = node.process(
            数据帧=large_data,
            处理方法="方法1",
            参数值=1.0
        )
        
        end_time = time.time()
        
        # 确保在合理时间内完成
        assert end_time - start_time < 5  # 5秒内完成
        assert len(result[0]) == len(large_data)
    
    def test_data_integrity(self, node, sample_data):
        """测试数据完整性。"""
        original_shape = sample_data.shape
        
        result = node.process(
            数据帧=sample_data,
            处理方法="方法1",
            参数值=1.0
        )
        
        # 确保原始数据未被修改
        assert sample_data.shape == original_shape
        
        # 验证结果数据的完整性
        assert not result[0].isnull().any().any()
```

#### 集成测试

```python
def test_node_integration():
    """测试节点集成。"""
    from src.Nodes.ReadCSV import ReadCSV
    from src.Nodes.DropNA import DropNA
    from src.Nodes.NewDataNode import NewDataNode
    
    # 创建测试数据文件
    test_data = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [1, 2, 3, 4],
        'C': [1, 2, 3, 4]
    })
    test_file = "test_integration.csv"
    test_data.to_csv(test_file, index=False)
    
    try:
        # 模拟工作流
        reader = ReadCSV()
        cleaner = DropNA()
        processor = NewDataNode()
        
        # 执行流水线
        data = reader.process(文件路径=test_file)[0]
        clean_data = cleaner.process(数据帧=data)[0]
        result = processor.process(
            数据帧=clean_data,
            处理方法="方法1",
            参数值=1.0
        )[0]
        
        # 验证结果
        assert not result.empty
        assert not result.isnull().any().any()
        
    finally:
        # 清理测试文件
        import os
        if os.path.exists(test_file):
            os.remove(test_file)
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_nodes/test_data_nodes.py

# 运行特定测试类
pytest tests/test_nodes/test_data_nodes.py::TestNewDataNode

# 运行特定测试方法
pytest tests/test_nodes/test_data_nodes.py::TestNewDataNode::test_basic_functionality

# 生成覆盖率报告
pytest --cov=src --cov-report=html

# 详细输出
pytest -v

# 并行运行测试
pytest -n auto

# 只运行失败的测试
pytest --lf

# 运行性能测试
pytest -m performance
```

### 测试覆盖率要求

- **新功能**: 必须达到90%以上的测试覆盖率
- **核心功能**: 必须达到95%以上的测试覆盖率
- **边界条件**: 必须包含边界条件和异常情况测试
- **性能测试**: 关键算法必须包含性能测试

---

## 文档贡献

### 文档类型

1. **API文档**: 详细的接口说明
2. **用户指南**: 面向最终用户的教程
3. **开发者文档**: 技术实现细节
4. **示例教程**: 具体使用案例

### 文档规范

#### Markdown格式

```markdown
# 文档标题

简短的文档描述和目标读者说明。

## 目录

- [章节1](#章节1)
- [章节2](#章节2)

## 章节1

### 子章节1.1

内容描述...

#### 代码示例

```python
# Python代码示例
def example_function():
    return "Hello, World!"
```

#### 配置示例

```json
{
    "parameter": "value",
    "option": true
}
```

### 子章节1.2

| 参数名 | 类型 | 必需 | 默认值 | 说明 |
|--------|------|------|--------|------|
| param1 | str  | ✓    | ""     | 参数说明 |
| param2 | int  | ✗    | 0      | 可选参数 |

> **注意**: 重要提示信息

> **警告**: 需要特别注意的内容

## 章节2

内容...

---

*最后更新: 2025-01-XX*
```

#### 代码文档

```python
def complex_function(
    data: pd.DataFrame,
    method: str,
    parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, Dict[str, float]]:
    """执行复杂的数据处理操作。
    
    这个函数实现了多种数据处理算法，支持不同的参数配置。
    适用于大规模数据集的批处理场景。
    
    Args:
        data: 输入的DataFrame，必须包含数值列
        method: 处理方法，支持的选项:
            - 'standard': 标准处理方法
            - 'robust': 鲁棒处理方法
            - 'custom': 自定义处理方法
        parameters: 算法参数字典，包含:
            - 'threshold': float, 阈值参数 (0.0-1.0)
            - 'iterations': int, 迭代次数 (1-100)
            - 'normalize': bool, 是否标准化
    
    Returns:
        一个元组包含:
        - 处理后的DataFrame
        - 包含处理统计信息的字典
    
    Raises:
        ValueError: 当输入数据格式不正确时
        KeyError: 当必需的参数缺失时
        RuntimeError: 当算法执行失败时
    
    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> params = {'threshold': 0.5, 'iterations': 10, 'normalize': True}
        >>> result, stats = complex_function(data, 'standard', params)
        >>> print(f"处理了 {len(result)} 行数据")
        处理了 3 行数据
    
    Note:
        这个函数会修改输入数据的副本，不会影响原始数据。
        对于大数据集，建议使用 'robust' 方法以获得更好的性能。
    
    See Also:
        simple_function: 简化版本的处理函数
        batch_process: 批处理版本
    """
    # 实现代码
    pass
```

### 文档审查清单

- [ ] 语法和拼写检查
- [ ] 代码示例可以运行
- [ ] 链接有效性检查
- [ ] 图片和图表清晰
- [ ] 目录结构合理
- [ ] 交叉引用正确
- [ ] 版本信息更新

---

## 问题报告

### 报告Bug

在报告bug之前，请：

1. **搜索现有问题**: 检查是否已有相同问题
2. **确认版本**: 使用最新版本重现问题
3. **简化场景**: 创建最小重现示例

### Bug报告模板

```markdown
## Bug描述

简洁清晰地描述bug的现象。

## 重现步骤

1. 执行操作A
2. 设置参数B
3. 运行节点C
4. 观察到错误

## 预期行为

描述您期望发生的行为。

## 实际行为

描述实际发生的行为。

## 环境信息

- **操作系统**: Windows 10 / macOS 12 / Ubuntu 20.04
- **Python版本**: 3.9.7
- **DataFlow版本**: 0.0.1
- **ComfyUI版本**: 最新
- **相关依赖版本**: pandas 1.5.0, numpy 1.21.0

## 重现代码

```python
# 提供最小的重现代码
import pandas as pd
from src.Nodes.PCA import PCA

# 创建测试数据
data = pd.DataFrame(...)

# 重现问题的步骤
node = PCA()
result = node.process(...)
```

## 错误信息

```
完整的错误堆栈信息
```

## 附加信息

- 数据集大小
- 内存使用情况
- 相关日志
- 截图（如适用）

## 可能的解决方案

如果您有解决方案的想法，请在此描述。
```

---

## 功能请求

### 请求新功能

在提交功能请求前，请：

1. **检查现有功能**: 确认功能不存在
2. **搜索请求**: 查看是否有类似请求
3. **考虑通用性**: 功能是否对其他用户有用

### 功能请求模板

```markdown
## 功能描述

清晰描述您希望添加的功能。

## 使用场景

描述这个功能的具体使用场景和目标用户。

## 详细需求

### 输入要求
- 数据类型
- 参数配置
- 约束条件

### 输出要求
- 返回格式
- 性能要求
- 质量标准

### 界面要求
- 参数界面
- 可视化需求
- 用户交互

## 实现建议

如果您有实现思路，请在此描述：

- 算法选择
- 技术方案
- 依赖库
- 性能考虑

## 替代方案

描述您考虑过的其他解决方案。

## 优先级

- [ ] 低 - 有用但不紧急
- [ ] 中 - 重要功能
- [ ] 高 - 关键功能
- [ ] 紧急 - 阻塞性问题

## 愿意贡献

- [ ] 我愿意实现这个功能
- [ ] 我可以提供测试
- [ ] 我可以编写文档
- [ ] 我只是提出建议
```

---

## Pull Request流程

### 提交PR前的检查清单

- [ ] 代码遵循项目规范
- [ ] 所有测试通过
- [ ] 添加了必要的测试
- [ ] 更新了相关文档
- [ ] 提交信息符合规范
- [ ] 没有合并冲突
- [ ] PR描述清晰完整

### PR模板

```markdown
## 变更描述

简要描述这个PR的主要变更。

## 变更类型

- [ ] Bug修复
- [ ] 新功能
- [ ] 文档更新
- [ ] 性能优化
- [ ] 代码重构
- [ ] 测试改进

## 相关Issue

- Closes #123
- Related to #456

## 测试

描述您如何测试了这些变更：

- [ ] 单元测试
- [ ] 集成测试
- [ ] 手动测试
- [ ] 性能测试

### 测试环境

- 操作系统: 
- Python版本: 
- 测试数据: 

## 截图

如果适用，添加截图来说明变更。

## 检查清单

- [ ] 我的代码遵循项目的代码规范
- [ ] 我已经进行了自我审查
- [ ] 我已经添加了必要的注释
- [ ] 我已经更新了相关文档
- [ ] 我的变更没有产生新的警告
- [ ] 我已经添加了测试来证明修复有效或功能正常
- [ ] 新的和现有的单元测试都通过

## 破坏性变更

如果这是一个破坏性变更，请描述：

- 什么被改变了
- 为什么需要这个变更
- 如何迁移现有代码

## 附加信息

任何其他相关信息。
```

### PR审查流程

1. **自动检查**: CI/CD流水线自动运行
2. **代码审查**: 维护者进行代码审查
3. **测试验证**: 确保所有测试通过
4. **文档检查**: 验证文档更新
5. **最终批准**: 获得维护者批准
6. **合并**: 合并到目标分支

### 审查标准

#### 代码质量
- 代码清晰易读
- 遵循项目规范
- 适当的错误处理
- 性能考虑

#### 测试覆盖
- 充分的测试覆盖
- 边界条件测试
- 错误情况测试
- 性能测试（如需要）

#### 文档完整性
- API文档更新
- 用户指南更新
- 代码注释充分
- 变更日志更新

---

## 社区支持

### 获取帮助

- **GitHub Issues**: 报告bug和功能请求
- **GitHub Discussions**: 一般讨论和问答
- **邮件**: koren.cai.cy@gmail.com
- **ComfyUI Discord**: 社区讨论

### 贡献认可

我们重视每一个贡献，无论大小：

- **代码贡献者**: 在CONTRIBUTORS.md中列出
- **文档贡献者**: 在文档中署名
- **Bug报告者**: 在发布说明中感谢
- **功能建议者**: 在功能实现时致谢

### 社区活动

- **月度会议**: 讨论项目进展和规划
- **代码审查**: 互相学习和改进
- **文档马拉松**: 集中改进文档
- **黑客松**: 快速开发新功能

---

## 许可证

通过向本项目贡献代码，您同意您的贡献将在与项目相同的[MIT许可证](LICENSE)下授权。

---

## 致谢

感谢所有为DataFlow项目做出贡献的开发者！

特别感谢：
- ComfyUI社区的技术支持
- 开源社区的宝贵反馈
- 所有测试用户的耐心和建议

---

*我们期待您的贡献，让DataFlow变得更好！*