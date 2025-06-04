import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

app.registerExtension({
    name: "Comfy.ShowAny",
    async nodeCreated(node) {
        if (node.comfyClass === "ShowAny") {
            const TextWidget = node.addWidget("STRING", "Text", "");
            node.onExecuted = function(output) {
                TextWidget.value = output.text[0];
            }
        }
    }
});