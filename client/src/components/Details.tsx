import * as React from 'react';

import { ServerData } from '../interface';

class Details extends React.Component<ServerData> {
  render() {
    return (
      <div>
        <p>{this.props.name} - {this.props.id}</p>
        {this.props.file && <a href={`http://localhost:5000/${this.props.file}`} download>Image</a> }
      </div>
    )
  }
}

export default Details;