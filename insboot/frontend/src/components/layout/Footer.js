import React, { Component } from "react";
import { Layout } from "antd";

const { Footer } = Layout;

export default class ShizfFooter extends Component {
  render() {
    return <Footer style={footerStyle}>决定做了就认真对待</Footer>;
  }
}

const footerStyle = {
  textAlign: "center",
  bottom: "10px",
  width: "100%",
  fontFamily: "microsoft-YAHEI",
  color: "red"
};
