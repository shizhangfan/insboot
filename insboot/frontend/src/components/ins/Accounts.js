import React, { Component } from "react";
import { Table, Button, Modal, Form } from "antd";
import { connect } from "react-redux";

import {
  getInsAccounts,
  addInsAccount,
  deleteInsAccount,
  selectInsAccount,
  updateInsAccount
} from "../../actions/ins/accounts";
import UserForm from "./accounts/UserForm";

class Accounts extends Component {
  state = {
    visible: false,
    edit: false
  };

  componentDidMount() {
    this.props.getInsAccounts();
  }

  showUserModal = (operation, account) => {
    this.setState({
      visible: true,
      edit: operation === "add" ? false : true
    });
    if (operation === "edit") {
      this.props.selectInsAccount(account);
    }
  };

  handleCancel = () => {
    this.setState({ visible: false });
  };

  handleOk = value => {
    this.setState({ visible: false });
    const { edit } = this.state;
    if (edit) {
      this.props.updateInsAccount(value);
    } else {
      this.props.addInsAccount(value);
    }
  };

  delete = id => {
    this.props.deleteInsAccount(id);
  };

  render() {
    const columns = [
      {
        title: "ID",
        dataIndex: "id",
        key: "id"
      },
      {
        title: "邮箱地址",
        dataIndex: "email",
        key: "email"
      },
      {
        title: "手机号码",
        dataIndex: "phone",
        key: "phone"
      },
      {
        title: "密码",
        dataIndex: "password",
        key: "password"
      },
      {
        title: "标签",
        dataIndex: "tag_name",
        key: "tag_name"
      },
      {
        title: "状态",
        dataIndex: "status",
        key: "status"
      },
      {
        title: "粉丝数",
        dataIndex: "followers",
        key: "followers",
        render: (text, record) => {
          <span>{`${text}=${record.followers}`}</span>;
        }
      },
      {
        title: "编辑",
        key: "edit",
        render: (text, record) => (
          <span>
            <Button
              type="primary"
              onClick={this.showUserModal.bind(this, "edit", record)}
            >
              编辑
            </Button>
          </span>
        )
      },
      {
        title: "删除",
        key: "delete",
        render: (text, record) => (
          <span>
            <Button type="danger" onClick={this.delete.bind(this, record.id)}>
              删除
            </Button>
          </span>
        )
      }
    ];

    const { visible, edit } = this.state;

    return (
      <div>
        <Button
          type="primary"
          style={{ marginBottom: 16, marginTop: 20, marginLeft: 20 }}
          onClick={this.showUserModal.bind(this, "add")}
        >
          添加账号
        </Button>
        <Table
          columns={columns}
          dataSource={this.props.insAccounts}
          rowKey="id"
        />
        <WrappedAccountForm
          visible={visible}
          edit={edit}
          handleCancel={this.handleCancel}
          handleOk={this.handleOk}
          addInsAccount={this.props.addInsAccount}
        />
      </div>
    );
  }
}

const mapStateToProps = state => ({
  insAccounts: state.insAccounts.insAccounts
});

const WrappedAccountForm = Form.create({ name: "user" })(UserForm);

export default connect(
  mapStateToProps,
  {
    getInsAccounts,
    addInsAccount,
    deleteInsAccount,
    selectInsAccount,
    updateInsAccount
  }
)(Accounts);
