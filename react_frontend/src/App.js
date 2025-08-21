//REFERENCED FROM  https://www.geeksforgeeks.org/reactjs/reactjs-componentdidmount-method/
// SAMIP REGMI
import React, { Component } from "react";
class UsersList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      details: []  
    };
  }

  componentDidMount() {
    fetch("http://localhost:8000/api/signup/") 
      .then(res => res.json())
      .then(data => {
        this.setState({ details: data.users });
      });
  }

  render() {
    return (
      <div>
        <h2>Users List</h2>
        <ul>
          {this.state.details.map(user => (
            <li key={user.userId}>
              {user.firstname} {user.lastname} - {user.email} - {user.username} - {user.phonenumber}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default UsersList;
