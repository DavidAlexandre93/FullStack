import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { v4 as uuidv4 } from 'uuid';

const UserForm = (props) => {
  const [user, setUser] = useState(() => {
    return {
      username: props.user ? props.user.username : '',
      name: props.user ? props.user.name : '',
      email: props.user ? props.user.email : '',
      password: props.user ? props.user.password : '',
      date: props.user ? props.user.date : ''
    };
  });

  const [errorMsg, setErrorMsg] = useState('');
  const { username, name, password, email } = user;

  const handleOnSubmit = (event) => {
    event.preventDefault();
    const values = [username, name, password, email];
    let errorMsg = '';

    const allFieldsFilled = values.every((field) => {
      const value = `${field}`.trim();
      return value !== '' && value !== '0';
    });

    if (allFieldsFilled) {
      const user = {
        id: uuidv4(),
        username,
        name,
        password,
        email,
        date: new Date()
      };
      props.handleOnSubmit(user);
    } else {
      errorMsg = 'Please fill out all the fields.';
    }
    setErrorMsg(errorMsg);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      // case 'email':
      //   if (value === '' || parseInt(value) === +value) {
      //     setUser((prevState) => ({
      //       ...prevState,
      //       [name]: value
      //     }));
      //   }
      //   break;
      case 'password':
        if (value === '' || value.match(/^\d{1,}(\.\d{0,2})?$/)) {
          setUser((prevState) => ({
            ...prevState,
            [name]: value
          }));
        }
        break;
      default:
        setUser((prevState) => ({
          ...prevState,
          [name]: value
        }));
    }
  };

  return (
    <div className="main-form">
      {errorMsg && <p className="errorMsg">{errorMsg}</p>}
      <Form onSubmit={handleOnSubmit}>
        <Form.Group controlId="name">
          <Form.Label>UserName</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="username"
            value={username}
            placeholder="Enter username"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="name"
            value={name}
            placeholder="Enter name of name"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            className="input-control"
            type="text"
            name="email"
            value={email}
            placeholder="Enter available email"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control
            className="input-control"
            type="password"
            name="password"
            value={password}
            maxLength={8}
            placeholder="Enter password of user"
            onChange={handleInputChange}
          />
        </Form.Group>
        <Button variant="primary" type="submit" className="submit-btn">
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default UserForm;
