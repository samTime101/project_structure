// REFERENCED FROM https://www.geeksforgeeks.org/reactjs/how-to-connect-django-with-reactjs/
// ADDED BY SAMIP REGMI

import React from 'react';
import axios from 'axios';

class App extends React.Component {

    state = {
        details : [],
    }

    componentDidMount() {

        let data ;

        axios.get('http://localhost:8000/api/signup/')
        .then(res => {
            data = res.data;
            this.setState({
                details : data    
            });
        })
        .catch(err => {})
    }

  render() {
    return(
      <div>
            {this.state.details.map((detail, id) =>  (
            <div key={id}>
            <div >
                  <div >
                        <h1>REACT APP HELLOOOO</h1>
                        <h1>DATA FROM API</h1>

                        <footer > 
                        <p>username: {detail.username}</p>
                        <p>email: {detail.email}</p>
                        <p>first name: {detail.firstname}</p>
                        <p>last name: {detail.lastname}</p>
                        <p>is active: {detail.is_active ? 'Yes' : 'No'}</p>
                        <p>is staff: {detail.is_staff ? 'Yes' : 'No'}</p>
                        <p>{detail.is_superuser ? 'Yes' : 'No'}</p>
                        </footer>
                  </div>
            </div>
            </div>
            )
        )}
      </div>
      );
  }
}

export default App;