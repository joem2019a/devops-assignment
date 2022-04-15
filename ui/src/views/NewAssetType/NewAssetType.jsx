import React from 'react';
import { useHistory } from 'react-router-dom';

import { Form, Button } from 'react-bootstrap';
import axios from 'axios';

import style from './new-type.module.scss';

const NewAssetType = () => {

  const history = useHistory();

  const submit = async (event) => {

    const data = {
      name: event.target.elements.name.value,
      description: event.target.elements.description.value,
      cost: event.target.elements.cost.value,
    }

    try {
      await axios.post('/asset-type', data);
      history.replace('/admin');
    } catch (e) {
      console.error(e)
    }
  }

  return (
    <section id="new-asset-type" className={style.newType}>
      <Form onSubmit={(e) => {e.preventDefault(); submit(e); }}>
        <Form.Group className="mb-3" controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control 
            type="text" 
            name="name"
            placeholder="Name"
            required
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="description">
          <Form.Label>Description</Form.Label>
          <Form.Control 
            type="text" 
            name="description"
            placeholder="Description"
            required
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="cost">
          <Form.Label>Cost</Form.Label>
          <Form.Control 
            type="number" 
            name="cost"
            placeholder="0"
            required
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Add
        </Button>
      </Form>
    </section>
  )
}

export default NewAssetType;
