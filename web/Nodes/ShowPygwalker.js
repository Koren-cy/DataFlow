import { app } from "/scripts/app.js";

app.registerExtension({
    name: "dataflow.ShowPygwalker",
    
    async nodeCreated(node) {
        if (node.comfyClass === "ShowPygwalker") {

            // 设置节点大小
            const width = 720;
            const height = 360;
            node.size =[width,height];

            // 创建DOM容器元素
            const domContainer = document.createElement("div");
            domContainer.className = "comfy-dom-container";
            domContainer.style.border = "1px solid #222";
            domContainer.style.borderRadius = "4px";
            domContainer.style.padding = "10px";
            domContainer.style.overflow = "auto";
            domContainer.style.minHeight = "50px";
            domContainer.style.width = "100%";
            domContainer.style.boxSizing = "border-box";
            domContainer.innerHTML = "<div></div>";
            
            // 使用addDOMWidget方法添加DOM容器到节点
            node.addDOMWidget("dom_widget", "DOM Display", domContainer);

            node.onExecuted = function(message) {
                if (message) {
                    domContainer.innerHTML =  message.content[0];;
                };
            };
        }
    },
});

// 添加自定义样式
const style = document.createElement("style");
style.textContent = `
    .comfy-dom-container {
        font-family: Arial, sans-serif;
        line-height: 1.5;
        width: 100%;
        box-sizing: border-box;
    }
`;
document.head.appendChild(style);