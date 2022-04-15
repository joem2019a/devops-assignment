import React, { useEffect, useState } from 'react';
import { useHistory, useLocation } from 'react-router-dom';

import { Form, Button, Dropdown, DropdownButton } from 'react-bootstrap';
import axios from 'axios';

import style from './change-asset-assignment.module.scss';

const ChangeAssetAssignment = () => {

  const history = useHistory();
  const { search } = useLocation();
  const assetid = new URLSearchParams(search).get('assetid');

  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({
    userId: undefined,
  })

  const getUsers = async () => {
    try {
      const response = await axios.get('/users', {
        params: {
          admin: true
        }
      });
      setUsers(response.data);
    } catch (e) {
      console.error(e);
    }
  }

  useEffect(() => {
    getUsers();
  }, [])

  const submit = async () => {
    if (form.userId) {
      try {
        await axios.put(
          `/asset/${assetid}`, 
          {
            user_id: form.userId,
          }
        )
        history.push('/admin');
      } catch (e) {
        console.error(e);
      }
    }
  }

  return (
    <section id="change-asset-assignment" className={style.changeAssetAssignment}>
      <Form onSubmit={(e) => {e.preventDefault(); submit(); }}>
        <DropdownButton
          variant="outline-primary"
          title="User"
          id="user-dropdown"
        >
          {users.map(({ user_id, username }) => (
            <Dropdown.Item 
              key={user_id} 
              onClick={() => setForm({ ...form, userId: user_id })}
            >
              {username}
            </Dropdown.Item>
          ))}
        </DropdownButton>
        <p>Selected: {users.filter(({ user_id }) => user_id === form.userId)[0]?.username ?? 'Please select a user.'}</p>
        <Button variant="primary" type="submit" disabled={!form.userId}>
          Submit
        </Button>
      </Form>
    </section>
  )
}

export default ChangeAssetAssignment;
