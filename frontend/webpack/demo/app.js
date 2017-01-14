import React from "react";
import ReactDOM from "react-dom";
import Hello from "./hello";
import Name from "./react/name.js"
var nm = require("./react/name.js");

ReactDOM.render(
  // 下面是几种不同的模块导入使用方式
  nm.yt,  //<Name name="Silly" />, //<Hello name="World2" />,
  document.getElementById('root')
);
