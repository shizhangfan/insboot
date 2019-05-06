import React, { Component } from "react";
import ReactDOM from "react-dom";

import Container from "./layout/Container";
import "style-loader!css-loader!antd/dist/antd.css";
import "style-loader!css-loader!./App.css"

import { Provider } from "react-redux";
import store from "../store";

export default class App extends Component {
  render() {
    return (
      <Provider store={store} style={{ height: "100%"}}>
        <Container style={{ height: "100%"}}/>
      </Provider>
    );
  }
}

ReactDOM.render(<App style={{ height: "100%"}}/>, document.getElementById("app"));
