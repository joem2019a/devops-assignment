import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

import { Button } from 'react-bootstrap';
import axios from 'axios';

import Table from '../../components/Table/Table';
import style from './admin.module.scss';

const Admin = () => {

  const history = useHistory();

  const [requests, setRequests] = useState([]);
  const [assetTypes, setAssetTypes] = useState([]);
  const [assets, setAssets] = useState([]);
  const [users, setUsers] = useState([]);

  const getData = async () => {
    try {
      const responses = await Promise.all([
        '/asset-requests',
        '/asset-types',
        '/assets',
        '/users',
      ].map((path) => axios.get(path, { params: { admin: true } })))

      setRequests(responses[0].data)
      setAssetTypes(responses[1].data.map((type) => ({ ...type, cost: `£${type.cost / 100}` })))
      setAssets(responses[2].data)
      setUsers(responses[3].data.map((user) => ({ ...user, is_admin: user.is_admin.toString() })))
    } catch (e) {
      console.error(e)
    }
  }

  const toggleAdminStatus = async (index) => {
    const user = users[index];
    try {
      await axios.post(`/user/${user.user_id}/admin`, {
        is_admin: user.is_admin === 'true' ? false : true,
      })
      await getData();
    } catch (e) {
      console.error(e)
    }
  }

  const deleteItem = async(path) => {
    try {
      await axios.delete(path);
      await getData();
    } catch (e) {
      console.error(e);
    }
  }

  const toggleComplete = async (index) => {
    try {
      await axios.put(`/asset-request/${requests[index].asset_request_id}`, {
        status: requests[index].status === 'Complete' ? 'InProgress' : 'Complete',
      });
      await getData();
    } catch (e) {
      console.error(e);
    }
  }

  useEffect(() => {
    getData();
  }, [])


  return (
    <section id="home">
      <div className={style.header}>
        <h1>Admin Dashboard</h1>
        <p>Manage assets, asset types, asset requests and users.</p>
      </div>
      <hr/>
      <div className={style.adminSection}>
        <h2>Asset Requests</h2>
        <Table 
          columns={[
            ['Request ID', 'asset_request_id'],
            ['Asset Type', 'asset_type.name'],
            ['Notes', 'notes'],
            ['Status', 'status'],
          ]}
          data={requests}
          actions={[
            ['Toggle Complete', toggleComplete],
            ['Delete', (i) => deleteItem(`/asset-request/${requests[i].asset_request_id}`)],
          ]}
        />
      </div>
      <div className={style.adminSection}>
        <div className={style.buttonTitle}>
          <h2>Asset Types</h2>
          <Button variant="outline-primary" onClick={() => history.push('/admin/new-asset-type')}>
            New Asset Type
          </Button>
        </div>
        <Table 
          columns={[
            ['Asset Type ID', 'asset_type_id'],
            ['Name', 'name'],
            ['Description', 'description'],
            ['Cost', 'cost'],
          ]}
          data={assetTypes}
          actions={[
            ['Delete', (i) => deleteItem(`/asset-type/${assetTypes[i].asset_type_id}`)],
          ]}
        />
      </div>
      <div className={style.adminSection}>
        <div className={style.buttonTitle}>
          <h2>Assets</h2>
          <Button variant="outline-primary" onClick={() => history.push('/admin/new-asset')}>
            New Asset
          </Button>
        </div>
        <Table 
          columns={[
            ['Asset ID', 'asset_id'],
            ['Asset Type', 'asset_type.name'],
            ['Description', 'asset_type.description'],
            ['Assigned To', 'user.username'],
          ]}
          data={assets}
          actions={[
            ['Change Asssignment', (i) => history.push(`/admin/change-asset-assignment?assetid=${assets[i].asset_id}`)],
            ['Delete', (i) => deleteItem(`/asset/${assets[i].asset_id}`)],
          ]}
        />
      </div>
      <div className={style.adminSection}>
        <h2>Users</h2>
        <Table 
          columns={[
            ['User ID', 'user_id'],
            ['Username', 'username'],
            ['Name', 'name'],
            ['Email', 'email'],
            ['Is Admin?', 'is_admin'],
          ]}
          data={users}
          actions={[
            ['Toggle Admin Status', toggleAdminStatus],
            ['Delete', (i) => deleteItem(`/user/${users[i].user_id}`)],
          ]}
        />
      </div>
    </section>
  )
}

export default Admin;
