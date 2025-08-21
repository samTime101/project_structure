// REFERENCED FROM https://medium.com/@mranwarali/how-to-create-a-signup-form-in-react-using-axios-to-send-user-data-to-a-custom-api-endpoint-e6240d04a3f9
// SAME AS Signup.js
// SAMIP REGMI
import React, { useState } from 'react';
import axios from 'axios';

const Signin = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

    const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
        const response = await axios.post('http://localhost:8000/api/signin/', {
        email:email,
        password:password,
        });

        setSuccess(response.data.message);
    } catch (err) {
        setError('An error occurred while trying to sign in. Please try again later.');
        console.error(err);
    }
    };


  return (
    <div>
      <h2>Signin</h2>
      <form onSubmit={handleSubmit}>
        <div>
        <label>Email:
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required/>
        </label>
        </div>
        <div>
        <label>Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
        </label>
        </div>
        <button type="submit">Signin</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
    </div>
  );
};

export default Signin;
