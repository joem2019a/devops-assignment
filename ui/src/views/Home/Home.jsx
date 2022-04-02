import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

import { Button } from 'react-bootstrap';
import axios from 'axios';

import { useAuth } from '../../services/authentication';
import Table from '../../components/Table/Table';
import style from './home.module.scss';

const Home = () => {

  const history = useHistory();

  const {
    currentUser: {
      name,
      isAdmin,
    }
  } = useAuth();

  const [assets, setAssets] = useState([]);
  const [requests, setRequests] = useState([]);

  const getData = async () => {
    try {
      const [assetsResponse, assetRequestsResponse] = await Promise.all([
        axios.get('/assets'), 
        axios.get('/asset-requests')
      ]);
      setAssets(assetsResponse.data)
      setRequests(assetRequestsResponse.data)
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
        <h1>Welcome, {name}</h1>
        <p>View assets assigned to you and request new ones.</p>
        {isAdmin && <Button variant="outline-primary" onClick={() => history.push('/admin')}>Admin</Button>}
      </div>
      <hr/>
      <div className={style.homeSection}>
        <h2>Your Assets</h2>
        <Table 
          columns={[
            ['Asset ID', 'asset_id'],
            ['Asset Type', 'asset_type.name'],
            ['Description', 'asset_type.description'],
          ]}
          data={assets}
        />
      </div>
      <div className={style.homeSection}>
        <div className={style.requestsTitle}>
          <h2>Your Requests</h2>
          <Button variant="outline-primary" onClick={() => history.push('/new-asset-request')}>
            New Request
          </Button>
        </div>
        <Table 
          columns={[
            ['Request ID', 'asset_request_id'],
            ['Asset Type', 'asset_type.name'],
            ['Notes', 'notes'],
            ['Status', 'status'],
          ]}
          data={requests}
        />
      </div>
    </section>
  )
}

export default Home;
