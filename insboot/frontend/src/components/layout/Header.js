import React, { Component } from "react";
import { Layout, Menu } from "antd";

const { Header } = Layout;

class ShizfHeader extends Component {
  render() {
    return (
      <Header className="header">
        <div className="logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={["1"]}
          style={{ lineHeight: "64px" }}
        >
          <Menu.Item key="1">自动化工具</Menu.Item>
          <Menu.Item key="2">笔记</Menu.Item>
          <Menu.Item key="3">账本</Menu.Item>
          <Menu.Item key="4">日记</Menu.Item>
        </Menu>
      </Header>
    );
  }
}

export default ShizfHeader;
