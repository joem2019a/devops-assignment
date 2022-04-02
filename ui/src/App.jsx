import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import AuthProvider from './services/authentication';

import AppFrame from './components/AppFrame/AppFrame';
import Home from './views/Home/Home'
import NewRequest from './views/NewRequest/NewRequest'
import Admin from './views/Admin/Admin'
import Authentication from './views/Authentication/Authentication'

const App = () => {


  return (
    <BrowserRouter>
      <AuthProvider>
        <AppFrame>
          <Switch>
            <Route exact path="/auth"><Authentication /></Route>
            <Route exact path="/"><Home/></Route>
            <Route exact path="/admin"><Admin /></Route>
            <Route exact path="/new-asset-request"><NewRequest /></Route>
          </Switch>
        </AppFrame>
      </AuthProvider>
    </BrowserRouter>
  )
}

export default App;
