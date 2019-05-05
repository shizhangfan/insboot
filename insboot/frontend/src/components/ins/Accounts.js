import React, { Component } from "react";
import { Table, Button, Modal } from "antd";
import { connect } from "react-redux";

import { getInsAccounts } from "../../actions/ins/accounts";

class Accounts extends Component {
  state = {
    visible: false
  };

  componentDidMount() {
    this.props.getInsAccounts();
  }

  showAddUserModal = () => {
    this.setState({ visible: true });
  };

  handleCancel = () => {
    this.setState({ visible: false });
  };

  handleOk = () => {
    this.setState({ visible: false });
  };

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
      <div>
        <Button
          type="primary"
          style={{ marginBottom: 16, marginTop: 20, marginLeft: 20 }}
          onClick={this.showAddUserModal}
        >
          添加账号
        </Button>
        <Table
          columns={columns}
          dataSource={this.props.insAccounts}
          rowKey="id"
        />
        <Modal
          title="Basic Modal"
          visible={this.state.visible}
          onOk={this.handleOk}
          onCancel={this.handleCancel}
        />
      </div>
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
