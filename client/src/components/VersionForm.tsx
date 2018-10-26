import * as React from 'react';

import { Popup, ServerData, ServerResponse } from '../interface';

import axios from '../axios';

class VersionForm extends React.Component<Popup> {
  state = {
    value: '',
    file: ''
  };

  handleChange = (event) => {
    this.setState({
      value: event.target.value
    });
  }

  onChange = (e) => {
    this.setState({ file: e.target.files[0] })
  }

  handleSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData();
    const config = {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }
    formData.append('file', this.state.file);

    axios.post<ServerData>(`/apps/${this.props.appId}/${event.target.vers.value}`, formData, config).then(
      (res: ServerResponse) => {
        if (res.data) {
          this.props.updateParent();
        } else {
          alert('Already exists');
        }
      });
  }

  render() {
    return (
      <React.Fragment>
        <div className="modal fade" id="addVersionModal" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
          <div className="modal-dialog modal-dialog-centered" role="document">
            <div className="modal-content">
            <article className="mt-2 container">
              <section className="inner">
                <span className="close" onClick={this.props.closePopup} data-dismiss="modal">&times;</span>
                <form onSubmit={this.handleSubmit} className="row" encType="multipart/form-data">
                  <div className="col-12">
                    <label htmlFor="name">Version:</label>
                    <input type="text" name="vers" className="form-control"
                      value={this.state.value}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div className="col-12 mt-2">
                    <input type="file" onChange={this.onChange} />
                  </div>
                  <div className="col-12 justify-content-end">
                    <button className="btn btn-success float-right" type="submit">Submit</button>
                  </div>
                </form>
              </section>
            </article>
          </div>
        </div>
        </div>
      </React.Fragment>
    );
  }
}

export default VersionForm;
