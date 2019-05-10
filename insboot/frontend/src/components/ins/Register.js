import React, { Component } from 'react'
import { Card, Row, Col, Statistic, Button, Form, Input } from "antd";

const { TextArea } = Input;

export class Register extends Component {
    render() {
        return (
            <Card title="注册机">
                <Card
                    type="inner"
                    title="控制台"
                    extra={<a href="#">More</a>}
                >
                    <Row gutter={16}>
                        <Col span={12} style={{ textAlign: "center" }}>
                            <Button type="danger">停止</Button>
                        </Col>
                        <Col span={12} style={{ textAlign: "center" }}>
                            <Button type="primary">开始</Button>
                        </Col>
                    </Row>
                </Card>
                <Card
                    style={{ marginTop: 16 }}
                    type="inner"
                    title="统计信息"
                    extra={<a href="#">More</a>}
                >
                    <Row gutter={16}>
                        <Col span={6}>
                            <Statistic title="工作天数" value={112893} />
                        </Col>
                        <Col span={6}>
                            <Statistic title="注册总数" value={112893} />
                        </Col>
                        <Col span={6}>
                            <Statistic title="成功" value={112893} />
                        </Col>
                        <Col span={6}>
                            <Statistic title="失败" style={{ color: "red" }} value={112893} />
                        </Col>
                    </Row>
                </Card>
                <Card
                    style={{ marginTop: 16 }}
                    type="inner"
                    title="今日统计"
                    extra={<a href="#">More</a>}
                >
                    <Row gutter={16}>
                        <Col span={6}>
                            <Statistic title="计划数" value={112893} />
                        </Col>
                        <Col span={6}>
                            <Statistic title="已注册" value={112893} />
                        </Col>
                        <Col span={6}>
                            <Statistic title="成功" value={112893} />
                        </Col>
                        <Col span={6}>
                            <Statistic style={{ color: "red" }} title="失败" value={112893} />
                        </Col>
                    </Row>
                </Card>
                <Card
                    style={{ marginTop: 16 }}
                    type="inner"
                    title="工作设置"
                    extra={<a href="#">More</a>}
                >
                    <Form>
                        <Form.Item label="姓氏池">
                            <TextArea rows={4} />
                        </Form.Item>
                        <Form.Item label="名字池">
                            <TextArea rows={4} />
                        </Form.Item>
                        <Form.Item label="组合规则">
                            <Input placeholder="input placeholder" />
                        </Form.Item>
                        <Form.Item label="代理">
                            <Input placeholder="input placeholder" />
                        </Form.Item>
                    </Form>
                </Card>
            </Card>
        )
    }
}


export default Register
