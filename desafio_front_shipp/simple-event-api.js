(function (window, undefined) {
    "use strict";
    
    window.SEA = {
        addEventListener: function (node, type, handler) {
            if (node.addEventListener) {
                node.addEventListener(type, handler, false);
            } else if (node.attachEvent) {
                node.attachEvent("on" + type, handler);
            } else {
                node["on" + type] = handler;
            }
        },

        stopPropagation: function (e) {
            e || (e = event);

            if (e.stopPropagation) {
                e.stopPropagation();
            } else {
                e.cancelBubble = true;
            }
            
            return e;
        },

        preventDefault: function (e) {
            e || (e = event);
            
            if (e.preventDefault) {
                e.preventDefault();
            } else {
                e.returnValue = false;
            }
            
            return e;
        }
    };
}(window));

