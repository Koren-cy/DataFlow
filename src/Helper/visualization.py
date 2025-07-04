import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl


class Visualization:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.save_path = self.create_plots_folder()

        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun', 'Arial Unicode MS']  # 优先使用的中文字体列表
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        plt.rcParams['font.family'] = 'sans-serif'  # 使用无衬线字体

        self.setup_chinese_font()

    def create_plots_folder(self):
        """创建保存绘图的文件夹"""
        timestamp = datetime.now().strftime("%m%d_%H%M%S")
        folder_path = os.path.join(self.algorithm.CATEGORY, f"pca_results_{timestamp}")
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def setup_chinese_font(self):
        """设置中文字体"""
        # 检查操作系统
        if os.name == 'nt':  # Windows系统
            # Windows优先使用微软雅黑
            mpl.rc('font', family='Microsoft YaHei')
        else:  # 类Unix系统
            # 首选Arial Unicode MS
            mpl.rc('font', family='Arial Unicode MS')
        mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题