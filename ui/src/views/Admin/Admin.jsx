import React from 'react';
import { useHistory } from 'react-router-dom';

import { Button } from 'react-bootstrap';

import Table from '../../components/Table/Table';
import style from './admin.module.scss';

const Admin = () => {

  const history = useHistory();

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
          data={[]}
          // actions: change status, delete
        />
      </div>
      <div className={style.adminSection}>
        <div className={style.buttonTitle}>
          <h2>Asset Types</h2>
          <Button variant="outline-primary" onClick={() => history.push('/new-asset-type')}>
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
          data={[]}
          // actions: delete
        />
      </div>
      <div className={style.adminSection}>
        <div className={style.buttonTitle}>
          <h2>Assets</h2>
          <Button variant="outline-primary" onClick={() => history.push('/new-asset')}>
            New Asset
          </Button>
        </div>
        <Table 
          columns={[
            ['Asset ID', 'asset_id'],
            ['Asset Type', 'asset_type.name'],
            ['Description', 'asset_type.description'],
          ]}
          data={[]}
          // actions: unassign/assign to user, delete
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
          data={[]}
          // actions: make admin
        />
      </div>
    </section>
  )
}

export default Admin;
