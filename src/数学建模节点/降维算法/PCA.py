import pandas as pd
import numpy as np
from sklearn.decomposition import PCA as SklearnPCA
import matplotlib.pyplot as plt
import seaborn as sns
import os
from ...Helper.visualization import Visualization

class PCA:
    """
    主成分分析
    
    主成分分析是一种无监督的线性降维方法，旨在通过正交变换将高维数据投影到低维空间，同时最大化保留协方差。PCA能有效减少特征冗余、去除噪声，便于数据可视化与后续分析。
    
    如数据对尺度敏感，则需先标准化处理。
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "数据帧": ("DATAFRAME", {}),
                "目标维度": ("INT", {
                    "default": 2,
                    "min": 1,
                    "max": 100,
                    "step": 1,
                    "tooltip": "降维后的维度。"
                }),
            },
            "optional": {
                "处理列": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "要进行PCA降维的列名，多个列名用逗号分隔。留空则处理所有数值列。"
                }),
                "标签列": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "标签列列名。可视化中不同类别将用不同颜色表示。留空则用相同颜色。"
                }),
            },
        }

    RETURN_TYPES = ("DATAFRAME",)
    RETURN_NAMES = ("数据帧",)

    def process(self, 数据帧, 目标维度=2, 处理列="", 标签列=""):
        df = 数据帧.copy()
        
        # 处理类别标签
        labels = None
        if 标签列.strip():
            if 标签列.strip() not in df.columns:
                raise ValueError(f"标签列 '{标签列}' 不存在")
            labels = df[标签列.strip()].values
        
        # 确定要处理的列
        if 处理列.strip():
            target_cols = [col.strip() for col in 处理列.split(',') if col.strip()]
            invalid_cols = [col for col in target_cols if col not in df.columns]
            if invalid_cols:
                raise ValueError(f"列名不存在: {invalid_cols}")
            non_numeric_cols = [col for col in target_cols if not pd.api.types.is_numeric_dtype(df[col])]
            if non_numeric_cols:
                raise ValueError(f"以下列不是数值类型，无法进行PCA: {non_numeric_cols}")
        else:
            # 自动选择所有数值列，排除标签列
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            target_cols = [col for col in numeric_cols if col != 标签列.strip()]
            if not target_cols:
                raise ValueError("数据帧中没有数值列可以进行PCA")
        
        # 检查是否有空值
        if df[target_cols].isnull().any().any():
            raise ValueError(f"目标列中存在缺失值，请先处理缺失值。含缺失值的列: {df[target_cols].columns[df[target_cols].isnull().any()].tolist()}")
        
        # 检查目标维度是否合法
        if 目标维度 >= len(target_cols):
            raise ValueError(f"目标维度({目标维度})必须小于特征数量({len(target_cols)})")
        
        # 计算
        pca = SklearnPCA(n_components=目标维度, random_state=42)
        transformed_data = pca.fit_transform(df[target_cols])

        # 可视化
        class PCA_Visualization(Visualization):
            def plot_scree(self, pca):
                """绘制碎石图"""
                plt.figure(figsize=(5, 3))
                explained_variance_ratio = pca.explained_variance_ratio_
                cumulative_variance_ratio = np.cumsum(explained_variance_ratio)

                plt.plot(range(1, len(explained_variance_ratio) + 1), 
                        explained_variance_ratio, 'bo-', label='单个解释方差')
                plt.plot(range(1, len(cumulative_variance_ratio) + 1),
                        cumulative_variance_ratio, 'ro-', label='累积解释方差')

                plt.xlabel('主成分数量', fontsize=12)
                plt.ylabel('解释方差比', fontsize=12)
                plt.title('PCA碎石图', fontsize=14, pad=20)
                plt.legend(prop={'size': 10})
                plt.grid(True)
                plt.savefig(os.path.join(self.save_path, '碎石图.svg'), dpi=300, bbox_inches='tight')
                plt.close()

            def plot_scatter(self, transformed_data, labels=None):
                """绘制散点图"""
                # 设置颜色映射
                if labels is not None:
                    unique_labels = np.unique(labels)
                    colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_labels)))
                    color_dict = dict(zip(unique_labels, colors))

                if transformed_data.shape[1] >= 2:
                    # 2D散点图
                    plt.figure(figsize=(6, 4))
                    if labels is not None:
                        for label in unique_labels:
                            mask = labels == label
                            plt.scatter(transformed_data[mask, 0], 
                                      transformed_data[mask, 1],
                                      c=[color_dict[label]],
                                      label=str(label),
                                      alpha=0.6)
                        plt.legend(title='类别', bbox_to_anchor=(1.05, 1), loc='upper left', 
                                 prop={'size': 10}, title_fontsize=12)
                    else:
                        plt.scatter(transformed_data[:, 0], transformed_data[:, 1], alpha=0.6)

                    plt.xlabel('第一主成分 (PC1)', fontsize=12)
                    plt.ylabel('第二主成分 (PC2)', fontsize=12)
                    plt.title('PCA 2D散点图', fontsize=14, pad=20)
                    plt.grid(True)
                    plt.tight_layout()
                    plt.savefig(os.path.join(self.save_path, '2D散点图.svg'), dpi=300, bbox_inches='tight')
                    plt.close()

                if transformed_data.shape[1] >= 3:
                    # 3D散点图
                    fig = plt.figure(figsize=(7, 5))
                    ax = fig.add_subplot(111, projection='3d')

                    if labels is not None:
                        for label in unique_labels:
                            mask = labels == label
                            ax.scatter(transformed_data[mask, 0],
                                     transformed_data[mask, 1],
                                     transformed_data[mask, 2],
                                     c=[color_dict[label]],
                                     label=str(label),
                                     alpha=0.6)
                        ax.legend(title='类别', bbox_to_anchor=(1.05, 1), loc='upper left',
                                 prop={'size': 10}, title_fontsize=12)
                    else:
                        ax.scatter(transformed_data[:, 0],
                                  transformed_data[:, 1],
                                  transformed_data[:, 2],
                                  alpha=0.6)

                    ax.set_xlabel('PC1', fontsize=12)
                    ax.set_ylabel('PC2', fontsize=12)
                    ax.set_zlabel('PC3', fontsize=12)
                    ax.set_title('PCA 3D散点图', fontsize=14, pad=20)
                    plt.tight_layout()
                    plt.savefig(os.path.join(self.save_path, '3D散点图.svg'), dpi=300, bbox_inches='tight')
                    plt.close()

            def plot_heatmap(self, pca, feature_names):
                """绘制特征贡献度热力图"""
                components = pca.components_
                plt.figure(figsize=(6, 4))
                sns.heatmap(components.T, 
                           xticklabels=[f'PC{i+1}' for i in range(components.shape[0])],
                           yticklabels=feature_names,
                           cmap='coolwarm',
                           center=0,
                           annot=True,
                           fmt='.2f',
                           annot_kws={'size': 8})
                plt.title('PCA特征贡献度热力图', fontsize=14, pad=20)
                plt.xlabel('主成分', fontsize=12)
                plt.ylabel('特征', fontsize=12)
                plt.tight_layout()
                plt.savefig(os.path.join(self.save_path, '特征贡献度热力图.svg'), dpi=300, bbox_inches='tight')
                plt.close()

            def plot_biplot(self, pca, transformed_data, feature_names, labels=None):
                """绘制双标图"""
                plt.figure(figsize=(7, 5))

                # 绘制样本点
                if labels is not None:
                    unique_labels = np.unique(labels)
                    colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_labels)))
                    color_dict = dict(zip(unique_labels, colors))

                    for label in unique_labels:
                        mask = labels == label
                        plt.scatter(transformed_data[mask, 0],
                                  transformed_data[mask, 1],
                                  c=[color_dict[label]],
                                  label=str(label),
                                  alpha=0.6)
                    plt.legend(title='类别', bbox_to_anchor=(1.05, 1), loc='upper left',
                              prop={'size': 10}, title_fontsize=12)
                else:
                    plt.scatter(transformed_data[:, 0], transformed_data[:, 1], alpha=0.6)

                # 绘制特征向量
                coeff = pca.components_.T
                scale = np.abs(transformed_data).max() / np.abs(coeff).max() * 0.7

                for i, feature in enumerate(feature_names):
                    plt.arrow(0, 0, 
                             coeff[i, 0] * scale, 
                             coeff[i, 1] * scale,
                             color='r',
                             alpha=0.5,
                             head_width=scale*0.05)
                    plt.text(coeff[i, 0] * scale * 1.15, 
                            coeff[i, 1] * scale * 1.15, 
                            feature,
                            color='r',
                            ha='center',
                            va='center',
                            fontsize=10)

                plt.xlabel('PC1', fontsize=12)
                plt.ylabel('PC2', fontsize=12)
                plt.title('PCA双标图', fontsize=14, pad=20)
                plt.grid(True)

                # 等比例显示
                plt.axis('equal')
                plt.tight_layout()
                plt.savefig(os.path.join(self.save_path, '双标图.svg'), dpi=300, bbox_inches='tight')
                plt.close()

        visual = PCA_Visualization(self)

        # 碎石图
        visual.plot_scree(pca)
        # 散点图
        visual.plot_scatter(transformed_data, labels)
        # 热力图
        visual.plot_heatmap(pca, target_cols)
        # 双标图
        visual.plot_biplot(pca, transformed_data, target_cols, labels)
        
        # 创建新的列名并添加转换后的数据
        new_cols = [f'PC{i+1}' for i in range(目标维度)]
        for i, col in enumerate(new_cols):
            df[col] = transformed_data[:, i]
        
        # 删除原始列
        df = df.drop(columns=target_cols)
        
        return (df,)
