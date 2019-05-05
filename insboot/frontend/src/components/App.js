import React, { Component } from "react";
import ReactDOM from "react-dom";

import Container from "./layout/Container";
import "style-loader!css-loader!antd/dist/antd.css";

import { Provider } from "react-redux";
import store from "../store";

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Container />
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
