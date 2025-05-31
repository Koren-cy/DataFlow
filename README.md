# DataFlow

一个为快速数学建模而生的节点包

> [!NOTE]
> 本项目是使用[cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension)模板创建的。它可以帮助你开始编写自定义节点，而无需担心Python的设置问题。

## 快速开始

1. 安装 [ComfyUI](https://docs.comfy.org/get_started)。
1. 安装 [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. 在ComfyUI-Manager中查找此扩展。如果您手动安装，请将此仓库克隆到`ComfyUI/custom_nodes`目录下。
1. 重启ComfyUI。

# 功能特性

- 功能列表

## 开发

要安装开发依赖和pre-commit（将运行ruff钩子），请执行：

```bash
cd dataflow
pip install -e .[dev]
pre-commit install
```

上面的`-e`标志将导致"实时"安装，这意味着您对节点扩展所做的任何更改将在下次运行ComfyUI时自动被识别。

## 发布到Github

安装Github Desktop或按照这些[说明](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)设置ssh。

1. 创建与目录名称匹配的Github仓库。
2. 将文件推送到Git
```
git add .
git commit -m "project scaffolding"
git push
``` 

## 编写自定义节点

一个自定义节点示例位于[node.py](src/dataflow/nodes.py)中。要了解更多信息，请阅读[文档](https://docs.comfy.org/essentials/custom_node_overview)。


## 测试

本仓库在`tests/`目录中包含使用Pytest编写的单元测试。建议对您的自定义节点进行单元测试。

- [build-pipeline.yml](.github/workflows/build-pipeline.yml)将在任何开放的PR上运行pytest和linter
- [validate.yml](.github/workflows/validate.yml)将运行[node-diff](https://github.com/Comfy-Org/node-diff)来检查破坏性变更

## 发布到注册表

如果您希望与社区中的其他人分享此自定义节点，您可以将其发布到注册表。我们已经在`pyproject.toml`的`tool.comfy`下自动填充了一些字段，但请仔细检查它们是否正确。

您需要在 https://registry.comfy.org 上创建一个账户并创建API密钥令牌。

- [ ] 前往[注册表](https://registry.comfy.org)。登录并创建发布者ID（您的注册表个人资料中`@`符号后面的所有内容）。
- [ ] 将发布者ID添加到pyproject.toml文件中。
- [ ] 在注册表上创建用于从Github发布的API密钥。[说明](https://docs.comfy.org/registry/publishing#create-an-api-key-for-publishing)。
- [ ] 将其添加到您的Github仓库密钥中，作为`REGISTRY_ACCESS_TOKEN`。

Github操作将在每次git推送时运行。您也可以手动运行Github操作。完整说明[在此](https://docs.comfy.org/registry/publishing)。如果您有任何问题，请加入我们的[discord](https://discord.com/invite/comfyorg)！

