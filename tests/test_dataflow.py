#!/usr/bin/env python

"""用于 dataflow 包的测试。"""

import pytest
from src.dataflow.nodes import Example

@pytest.fixture
def example_node():
    """创建Example节点实例的fixture。"""
    return Example()

def test_example_node_initialization(example_node):
    """测试节点是否可以被实例化。"""
    assert isinstance(example_node, Example)

def test_return_types():
    """测试节点的元数据。"""
    assert Example.RETURN_TYPES == ("IMAGE",)
    assert Example.FUNCTION == "test"
    assert Example.CATEGORY == "Example"
