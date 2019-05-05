import React, { Component } from "react";
import { Table } from "antd";
import { connect } from "react-redux";

import { getInsAccounts } from "../../actions/ins/accounts";

class Accounts extends Component {
  componentDidMount() {
    this.props.getInsAccounts();
  }
  render() {
    const data = [
      {
        id: "1",
        email: "shijiangfan@qq.com",
        phone: "12345678901",
        password: "123456",
        status: 1,
        followers: 233
      }
    ];
    const columns = [
      {
        title: "ID",
        dataIndex: "id",
        key: "id"
      },
      {
        title: "email",
        dataIndex: "email",
        key: "email"
      },
      {
        title: "phone",
        dataIndex: "phone",
        key: "phone"
      },
      {
        title: "password",
        dataIndex: "password",
        key: "password"
      },
      {
        title: "status",
        dataIndex: "status",
        key: "status"
      },
      {
        title: "followers",
        dataIndex: "followers",
        key: "followers"
      }
    ];
    return (
      <Table
        columns={columns}
        dataSource={this.props.insAccounts}
        rowKey="id"
      />
    );
  }
}

const mapStateToProps = state => ({
  insAccounts: state.insAccounts.insAccounts
});

export default connect(
  mapStateToProps,
  { getInsAccounts }
)(Accounts);
