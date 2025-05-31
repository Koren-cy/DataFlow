from inspect import cleandoc
class Example:
    """
    一个示例节点

    类方法
    -------------
    INPUT_TYPES (dict):
        告诉主程序节点的输入参数。
    IS_CHANGED:
        可选方法, 用于控制节点何时重新执行。

    属性
    ----------
    RETURN_TYPES (tuple):
        输出元组中每个元素的类型。
    RETURN_NAMES (tuple):
        可选:输出元组中每个输出的名称。
    FUNCTION (str):
        入口点方法的名称。例如, 如果 FUNCTION = "execute", 则将运行Example().execute()
    OUTPUT_NODE ([bool]):
        如果此节点是从图表输出结果/图像的输出节点。SaveImage节点就是一个例子。
        后端会遍历这些输出节点, 并尝试执行其所有父节点（如果其父图正确连接）。
        如果不存在, 则假定为False。
    CATEGORY (str):
        节点在UI中应该出现的类别。
    execute(s) -> tuple || None:
        入口点方法。此方法的名称必须与属性 FUNCTION 的值相同。
        例如, 如果 FUNCTION = "execute", 则此方法的名称必须为 execute, 如果 FUNCTION = "foo" , 则必须为 foo。
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
            返回一个包含所有输入字段配置的字典。
            一些类型（字符串）:"MODEL"、"VAE"、"CLIP"、"CONDITIONING"、"LATENT"、"IMAGE"、"INT"、"STRING"、"FLOAT"。
            输入类型"INT"、"STRING"或"FLOAT"是节点上字段的特殊值。
            类型可以是一个用于选择的列表。

            返回:`dict`:
                - 键 input_fields_group(string):可以是required、hidden或optional。节点类必须具有属性`required`
                - 值 input_fields(dict):包含输入字段配置:
                    * 键 field_name(string):入口点方法参数的名称
                    * 值 field_config(tuple):
                        + 第一个值是表示字段类型的字符串或用于选择的列表。
                        + 第二个值是类型"INT"、"STRING"或"FLOAT"的配置。
        """
        return {
            "required": {
                "image": ("Image", { "tooltip": "This is an image"}),
                "int_field": ("INT", {
                    "default": 0,
                    "min": 0, #最小值
                    "max": 4096, #最大值
                    "step": 64, #滑块步长
                    "display": "number" #仅样式:显示为"number"或"slider"
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001, #四舍五入精度, 默认与步长相同。设为False可禁用四舍五入
                    "display": "number"}),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False, #设为True可使输入框样式类似ClipTextEncode节点
                    "default": "Hello World!"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "test"

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "Example"

    def test(self, image, string_field, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        #do some processing on the image, in this example I just invert it
        image = 1.0 - image
        return (image,)

    """
        如果任何输入发生变化, 节点将始终重新执行, 但
        此方法可用于强制节点再次执行, 即使输入没有变化。
        您可以使节点返回数字或字符串。此值将与节点上次执行时返回的值进行比较, 
        如果不同, 则节点将再次执行。
        此方法在核心仓库中用于LoadImage节点, 它们将图像哈希作为字符串返回, 如果图像哈希
        在执行之间发生变化, 则LoadImage节点将再次执行。
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""


# 一个包含所有要导出的节点及其名称的字典
# NOTE: 应使用全局唯一的名称
NODE_CLASS_MAPPINGS = {
    "Example": Example
}

# 一个包含节点人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example": "Example Node"
}
