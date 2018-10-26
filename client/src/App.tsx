import * as React from 'react';

import axios from './axios';

import Form from './components/Form';
import Item from './components/Item';

import { ServerData, ServerResponse } from './interface';

class App extends React.Component {
  state = {
    data: [],
    showPopup: false
  };

  togglePopup = () => {
    this.setState({
      showPopup: !this.state.showPopup
    });
  }

  componentDidMount() {
    this.loadData()
  }

  loadData = () => {
    axios.get(`/apps`).then(
      (res: ServerResponse) => {
        const data = res.data;
        console.log(res);
        this.setState({ data });
      });
  }

  render() {
    return (
      <div className="container">
        <article className="row">
          {this.state.data.map((app: ServerData) => <Item key={app.id} {...app} updateParent={this.loadData} />)}
          <button
            type="button" className="btn btn-primary" data-toggle="modal" data-target="#exampleModal"
          >
            Add Application
          </button>
          <Form closePopup={this.togglePopup} updateParent={this.loadData} />
        </article>
      </div>
    );
  }
}

export default App;
