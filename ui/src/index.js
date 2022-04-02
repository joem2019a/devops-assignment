import '@fontsource/open-sans/400.css';
import '@fontsource/open-sans/500.css';
import 'bootstrap/scss/bootstrap.scss';
import './index.scss';

import React from 'react';
import ReactDOM from 'react-dom';

import axios from 'axios';

import App from './App';

axios.defaults.baseURL = 'http://localhost:5000/api';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)
