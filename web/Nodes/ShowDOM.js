import { app } from "/scripts/app.js";

function DOM_TEMPLATE(X,Y,data){ 
    return `
        <script>var ShowDOMX=${X};</script>
        <script>var ShowDOMY=${Y};</script>
        <div>${data}</div>
    `;
}

app.registerExtension({
    name: "dataflow.ShowDOM",
    
    async nodeCreated(node) {
        if (node.comfyClass === "ShowDOM") {

            // 设置节点大小
            const width = 250;
            const height = 200;
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
            
            // 节点执行完成后的回调
            node.onExecuted = function(message) {
                if (message) {

                    var x="",y="",data="";
                    if(message.x){
                        x = message.x[0];
                    }
                    if(message.y){
                        y = message.y[0];
                    }
                    if(message.data){
                        data = message.data[0];
                    }

                    domContainer.innerHTML = DOM_TEMPLATE(x,y,data);
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