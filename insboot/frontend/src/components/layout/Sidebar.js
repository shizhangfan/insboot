import React, { Component, Fragment } from "react";
import { Layout, Menu, Icon } from "antd";
import { Link } from "react-router-dom";

const { SubMenu } = Menu;
const { Sider } = Layout;

export default class Sidebar extends Component {
  render() {
    return (
      <Fragment>
        <Sider width={200} style={{ background: "#fff" }}>
          <Menu
            mode="inline"
            defaultSelectedKeys={["1"]}
            defaultOpenKeys={["sub1"]}
            style={{ height: "100%", borderRight: 0 }}
          >
            <SubMenu key="sub1" title={<span>INS</span>}>
              <Menu.Item key="1">
                <Icon type="user" />
                账号
                <Link to="/ins/accounts" />
              </Menu.Item>
              <Menu.Item key="2">
                <Icon type="setting" />
                设置
                <Link to="/ins/settings" />
              </Menu.Item>
              <Menu.Item key="3">
                <Icon type="share-alt" />
                代理
                <Link to="/ins/proxies" />
              </Menu.Item>
              <Menu.Item key="4">
                <Icon type="rise" />
                注册机
                <Link to="/ins/register" />
              </Menu.Item>
              <Menu.Item key="5">
                <Icon type="area-chart" />
                报表
                <Link to="/ins/reports" />
              </Menu.Item>
            </SubMenu>
          </Menu>
        </Sider>
      </Fragment>
    );
  }
}
