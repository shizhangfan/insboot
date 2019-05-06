import React, { Component } from 'react';
import { Modal, Form, Input } from 'antd'

class UserForm extends Component {
    state = {
        email: "",
        phone: "",
        password: ""
    };

    onChange = e => {
        console.log(e.target.name)
        this.setState({[e.target.name]: [e.target.value]})
    }

    handleOk = () => {
        this.props.form.validateFields((err, value) => {
            if (!err) {
                this.props.handleOk(value)
            } else {
                console.log(err)
            }
        });
    }

    render () {
        const { getFieldDecorator } = this.props.form;
        const { email, phone, password } = this.state;

        const formItemLayout = {
            labelCol: {
              xs: { span: 24 },
              sm: { span: 4 },
            },
            wrapperCol: {
              xs: { span: 24 },
              sm: { span: 20 },
            },
          };
            
        return (
            <Modal
                title="Basic Modal"
                visible={this.props.visible}
                onOk={this.handleOk}
                onCancel={this.props.handleCancel}
            >
                <Form {...formItemLayout}>
                    <Form.Item
                        label="Email"
                    >
                        {
                            getFieldDecorator("email", {
                                rules: [{
                                    type: 'email', message: "The input is not valid email!"
                                }, {
                                    required: true, message: "Please input your email"
                                }]
                            })(
                                <Input onChange={this.onChange}/>
                            )
                        }
                    </Form.Item>

                    <Form.Item
                        label="Phone"
                    >
                        {
                            getFieldDecorator("phone")(
                                <Input onChange={this.onChange}/>
                            )
                        }
                    </Form.Item>

                    <Form.Item
                        label="Password"
                    >
                        {
                            getFieldDecorator("password", {
                                rules: [{
                                    type: 'string', message: "The input is not valid password!"
                                }, {
                                    required: true, message: "Please input your password"
                                }]
                            })(
                                <Input onChange={this.onChange}/>
                            )
                        }
                    </Form.Item>
                </Form>
            </Modal>
        )
    }
}

export default UserForm;