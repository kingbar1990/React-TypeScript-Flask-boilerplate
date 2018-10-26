import * as React from 'react';

import { ServerData } from '../interface';

import Details from './Details';
import VersionForm from './VersionForm';

class Item extends React.Component<ServerData> {
  state = {
    data: [],
    collapse: false,
    showPopup: false
  };

  getOneApplication = () => {
    this.setState({
      collapse: !this.state.collapse
    });
  }

  togglePopup = () => {
    this.setState({
      showPopup: !this.state.showPopup
    });
  }

  render() {
    return (
      <div className="col-12">
      <div className="row">
        <div className="col-12">
        <h3 onClick={this.getOneApplication}>{this.props.name}</h3>
        {this.state.collapse
          ? <article className="content">
            {this.props.versions.map((version: ServerData) => <Details key={version.id} {...version} name={this.props.name} />)}
            <button type="button" className="btn btn-info" data-toggle="modal" data-target="#addVersionModal">Add version</button>
            <VersionForm appId={this.props.id} closePopup={this.togglePopup} updateParent={this.props.updateParent} />
          </article>
          : null
        }
        </div>
        </div>
      </div>
    );
  }
}

export default Item;
