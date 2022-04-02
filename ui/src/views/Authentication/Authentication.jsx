import React, { useState, useCallback } from 'react';
import { useHistory } from 'react-router-dom';

import { Form, Button } from 'react-bootstrap';
import axios from 'axios';

import { useAuth } from '../../services/authentication';
import style from './authentication.module.scss';

const Authentication = () => {

  const history = useHistory();
  const { tokenChange } = useAuth();
  const [mode, setMode] = useState('login');

  const submit = useCallback(async (event) => {
    const data = {
      username: event.target.elements.username.value,
      password: event.target.elements.password.value,
    }

    if (mode === 'register') {
      data.email = event.target.elements.email.value;
      data.name = event.target.elements.name.value;
    }

    try {
      const { data: { access_token: token }} = await axios.post(`/auth/${mode}`, data);
      tokenChange(token);
      history.replace('/');
    } catch (e) {
      console.error(e);
    }
  }, [mode]) // eslint-disable-line

  return (
    <section id="authentication" className={style.loginForm}>
      {mode === 'login'
        ? (
          <Form onSubmit={(e) => {e.preventDefault(); submit(e); }}>
            <Form.Group className="mb-3" controlId="username">
              <Form.Label>Username</Form.Label>
              <Form.Control 
                type="text" 
                name="username"
                placeholder="Username"
                required
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="password">
              <Form.Label>Password</Form.Label>
              <Form.Control 
                type="password" 
                name="password" 
                placeholder="Password"
                required
              />
            </Form.Group>
            <Button variant="primary" type="submit">
              Log In
            </Button>
            <Button variant="outline-primary" onClick={() => setMode('register')}>
              Register
            </Button>
          </Form>
        ) : (
          <Form onSubmit={(e) => {e.preventDefault(); submit(e); }}>
            <Form.Group className="mb-3" controlId="username">
              <Form.Label>Username</Form.Label>
              <Form.Control 
                type="text" 
                name="username"
                placeholder="jbloggs"
                required
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="password">
              <Form.Label>Password</Form.Label>
              <Form.Control 
                type="password" 
                name="password" 
                placeholder="************"
                required
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="name">
              <Form.Label>Name</Form.Label>
              <Form.Control 
                type="text" 
                name="name"
                placeholder="Joe Bloggs"
                required
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="email">
              <Form.Label>Email</Form.Label>
              <Form.Control 
                type="email" 
                name="email"
                placeholder="joe.bloggs@gmail.com"
                required
              />
            </Form.Group>
            <Button variant="primary" type="submit">
              Register
            </Button>
            <Button variant="outline-primary" onClick={() => setMode('login')}>
              Sign in with Existing Account
            </Button>
          </Form>
        )
      }
    </section>
  )
}

export default Authentication;
