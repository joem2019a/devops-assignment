import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

import { Form, Button, Dropdown, DropdownButton } from 'react-bootstrap';
import axios from 'axios';

import style from './new-request.module.scss';

const NewRequest = () => {

  const history = useHistory();

  const [assetTypes, setAssetTypes] = useState([]);
  const [form, setForm] = useState({
    assetTypeId: undefined,
    notes: undefined,
  })

  const getAssetTypes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/asset-types');
      setAssetTypes(response.data);
    } catch (e) {
      console.error(e);
    }
  }

  useEffect(() => {
    getAssetTypes()
  }, [])

  const submit = async () => {
    if (form.assetTypeId) {

      try {
        const response = await axios.post(
          'http://localhost:5000/asset-request', 
          {
            asset_type_id: form.assetTypeId,
            notes: form.notes ?? ''
          }
        )
        history.push('/');
      } catch (e) {
        console.error(e);
      }
    }
  }

  return (
    <section id="new-request" className={style.newRequest}>
      <Form onSubmit={(e) => {e.preventDefault(); submit(); }}>
        <DropdownButton
          variant="outline-primary"
          title="Asset Type"
          id="asset-type-dropdown"
        >
          {assetTypes.map(({ asset_type_id, name }) => (
            <Dropdown.Item 
              key={asset_type_id} 
              onClick={() => setForm({ ...form, assetTypeId: asset_type_id })}
            >
              {name}
            </Dropdown.Item>
          ))}
        </DropdownButton>
        <p>Selected: {assetTypes.filter(({ asset_type_id }) => asset_type_id === form.assetTypeId)[0]?.name ?? 'Please select an asset type.'}</p>
        <Form.Group className="mb-3" controlId="formNotes">
          <Form.Label>Notes</Form.Label>
          <Form.Control type="text" placeholder="Optional: Enter notes to go with your request." />
        </Form.Group>
        <Button variant="primary" type="submit" disabled={!form.assetTypeId}>
          Submit
        </Button>
      </Form>
    </section>
  )
}

export default NewRequest;
