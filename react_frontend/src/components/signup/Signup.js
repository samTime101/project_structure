// REFERENCED FROM https://medium.com/@mranwarali/how-to-create-a-signup-form-in-react-using-axios-to-send-user-data-to-a-custom-api-endpoint-e6240d04a3f9
// SAMIP REGMI
import React, { useState } from 'react';
import axios from 'axios';

const Signup = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [username, setUsername] = useState('');
  const [phone, setPhone] = useState('');

  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

    const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
        const response = await axios.post('http://localhost:8000/api/signup/', {
        email:email,
        username:username,
        phonenumber: phone,
        firstname: firstName,
        lastname: lastName,
        password:password,
        });

        setSuccess(response.data.message);
    } catch (err) {
        setError('An error occurred while trying to sign up. Please try again later.');
        console.error(err);
    }
    };


  return (
    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <div>
        <label>Email:
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required/>
        </label>
        </div>
        <div>
        <label>First Name:
            <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} required/>
        </label>
        </div>
        <div>
        <label>Last Name:
            <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} required/>
        </label>
        </div>
        <div>
        <label>Username:
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required/>
        </label>
        </div>
        <div>
        <label>Phone:  
            <input type="tel" value={phone} onChange={(e) => setPhone(e.target.value)} required/>
        </label>
        </div>
        <div>
        <label>Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
        </label>
        </div>
        <button type="submit">Signup</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
    </div>
  );
};

export default Signup;