import React, { Component } from "react";
import { Modal, Form, Input, Select } from "antd";

import { connect } from "react-redux";
import { getInsTags } from "../../../actions/ins/tags";

const Option = Select.Option;

class UserForm extends Component {
  state = {
    email: "",
    phone: "",
    password: "",
    tag: ""
  };

  componentDidMount() {
    this.props.getInsTags();    
  }

  onChange = e => {
    this.setState({ [e.target.name]: [e.target.value] });
  };

  handleOk = () => {
    this.props.form.validateFields((err, value) => {
      if (!err) {
        const { edit, currentAccount } = this.props;
        if (edit) {
          const { id } = currentAccount;
          const { email, phone, password, tag } = value;
          const newData = { id, email, phone, password, tag };
          this.props.handleOk(newData);
        } else {
          this.props.handleOk(value);
        }        
      } else {
        console.log(err);
      }
    });
  };

  handleTagChange = value => {
    this.setState({ tag: value });
  };

  render() {
    const { getFieldDecorator } = this.props.form;
    const tags = this.props.insTags;
    const { edit, currentAccount } = this.props;
    
    const formItemLayout = {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 4 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 20 }
      }
    };

    return (
      <Modal
        title="用户信息"
        visible={this.props.visible}
        onOk={this.handleOk}
        onCancel={this.props.handleCancel}
      >
        <Form {...formItemLayout}>
          <Form.Item label="Email">
            {getFieldDecorator("email", {
              rules: [
                {
                  type: "email",
                  message: "The input is not valid email!"
                },
                {
                  required: true,
                  message: "Please input your email"
                }
              ],
              initialValue: edit ? currentAccount.email : ''
            })(<Input onChange={this.onChange} />)}
          </Form.Item>

          <Form.Item label="Phone">
            {getFieldDecorator("phone", {
              initialValue: edit ? currentAccount.phone : ''
            })(<Input onChange={this.onChange} />)}
          </Form.Item>

          <Form.Item label="Password">
            {getFieldDecorator("password", {
              rules: [
                {
                  type: "string",
                  message: "The input is not valid password!"
                },
                {
                  required: true,
                  message: "Please input your password"
                }
              ],
              initialValue: edit ? currentAccount.password : ''
            })(<Input onChange={this.onChange} />)}
          </Form.Item>

          <Form.Item label="Tag">
            {getFieldDecorator("tag", {
              rules: [
                {
                  required: true,
                  message: "请选择tag"
                }
              ],
              initialValue: edit ? currentAccount.tag : ''
            })(
              <Select 
                onChange={this.handleTagChange}>
                {tags.length &&
                  tags.map(t => <Option key={t.id} value={t.id}>{t.name}</Option>)}
              </Select>
            )}
          </Form.Item>
        </Form>
      </Modal>
    );
  }
}

const mapStatetoProps = state => ({
  insTags: state.insTags.insTags,
  currentAccount: state.insAccounts.currentAccount
});

export default connect(
  mapStatetoProps,
  { getInsTags }
)(UserForm);
