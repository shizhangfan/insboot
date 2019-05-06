import React, { Component, Fragment } from "react";
import { Route } from "react-router";
import { HashRouter as Router } from "react-router-dom";

import { Layout } from "antd";
import Header from "./Header";
import ShizfFooter from "./Footer";
import Sidebar from "./Sidebar";

import Accounts from "../ins/Accounts";
import Settings from "../ins/Settings";
import Reports from "../ins/Reports";
import Proxies from "../ins/Proxies";
import InsHome from "../ins/InsHome";

const { Content, Sider } = Layout;

class Container extends Component {
  render() {
    return (
      <Router>
        <Layout style={{ height: "100%"}}>
          <Header />
          <Layout>
            <Sidebar />
            <Layout>
              <Content>
                <Route exact path="/ins/" component={InsHome} />
                <Route exact path="/ins/accounts" component={Accounts} />
                <Route exact path="/ins/settings" component={Settings} />
                <Route exact path="/ins/proxies" component={Proxies} />
                <Route exact path="/ins/reports" component={Reports} />
              </Content>
            </Layout>
          </Layout>
          <ShizfFooter />
        </Layout>
      </Router>
    );
  }
}

export default Container;
