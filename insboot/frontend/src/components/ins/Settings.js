import React, { Component } from "react";
import { connect } from "react-redux";
import { Table } from "antd";

import { getSettings } from "../../actions/ins/settings";

export class Settings extends Component {
  componentDidMount() {
    this.props.getSettings();
  }
  render() {
    const columns = [
      {
        title: "ID",
        dataIndex: "id",
        key: "id"
      },
      {
        title: "name",
        dataIndex: "name",
        key: "name"
      },
      {
        title: "first_day",
        dataIndex: "first_day",
        key: "first_day"
      },
      {
        title: "second_day",
        dataIndex: "second_day",
        key: "second_day"
      }
    ];
    return (
      <Table columns={columns} dataSource={this.props.settings} rowKey="id" />
    );
  }
}

const mapStatetoProps = state => ({
  settings: state.insSettings.settings
});

export default connect(
  mapStatetoProps,
  { getSettings }
)(Settings);
