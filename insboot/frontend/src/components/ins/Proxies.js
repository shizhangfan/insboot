import React, {
  Component
} from "react";
import {
  Table
} from "antd";
import { connect } from "react-redux";
import { getProxies } from "../../actions/ins/proxies";

export class Proxies extends Component {
  componentDidMount() {
    this.props.getProxies();
  }
  render() {
    const columns = [
      {
        title: "序号",
        dataIndex: "id",
        key: "id"
      },
      {
        title: "名称",
        dataIndex: "name",
        key: "name"
      }
      ,
      {
        title: "IP",
        dataIndex: "ip",
        key: "ip"
      }
      ,
      {
        title: "端口",
        dataIndex: "port",
        key: "port"
      }
    ];
    return (
      <div>
        <Table
          columns={columns}
          dataSource={this.props.proxies}
          rowKey="id"
        />
      </div>);
  }
}

const mapStatetoProps = state => ({
  proxies: state.proxies.proxies
});

export default connect(mapStatetoProps, { getProxies })(Proxies);