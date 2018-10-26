import * as React from 'react';

import { Popup, ServerData, ServerResponse } from '../interface';

import axios from '../axios';

class Form extends React.Component<Popup> {
  state = {
    value: '',
  };

  handleChange = (event) => {
    this.setState({
      value: event.target.value
    });
  }

  handleSubmit = (event) => {
    event.preventDefault();

    axios.post<ServerData>(`/apps`, { name: event.target.name.value }).then(
      (res: ServerResponse) => {
        if (res.data.name) {
          this.props.updateParent();
        } else {
          alert('Already exists');
        }
      });
  }
  render() {
    return (
      <div className="modal fade" id="exampleModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div className="modal-dialog modal-dialog-centered" role="document">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title" id="exampleModalLabel">Add application</h5>
            <button type="button" className="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div className="modal-body">
          <form onSubmit={this.handleSubmit} className="row">
            <div className="col-12">
              <label htmlFor="name">Name:</label>
              <input type="text" name="name" className="form-control"
                value={this.state.value}
                onChange={this.handleChange}
              />
            </div>
            <div className="modal-footer">
            <button type="submit" className="btn btn-primary">Submit</button>
            <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </form>
          </div>
        </div>
      </div>
    </div>
    );
  }
}

export default Form;
