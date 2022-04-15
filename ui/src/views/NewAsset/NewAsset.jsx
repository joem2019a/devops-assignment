import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

import { Form, Button, Dropdown, DropdownButton } from 'react-bootstrap';
import axios from 'axios';

import style from './new-asset.module.scss';

const NewAsset = () => {

  const history = useHistory();

  const [assetTypes, setAssetTypes] = useState([]);
  const [form, setForm] = useState({
    assetTypeId: undefined,
  })

  const getAssetTypes = async () => {
    try {
      const response = await axios.get('/asset-types');
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
        await axios.post(
          '/asset', 
          {
            asset_type_id: form.assetTypeId,
          }
        )
        history.push('/admin');
      } catch (e) {
        console.error(e);
      }
    }
  }

  return (
    <section id="new-asset" className={style.newAsset}>
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
        <Button variant="primary" type="submit" disabled={!form.assetTypeId}>
          Add
        </Button>
      </Form>
    </section>
  )
}

export default NewAsset;
