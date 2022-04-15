import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import AuthProvider from './services/authentication';

import AppFrame from './components/AppFrame/AppFrame';
import Home from './views/Home/Home'
import NewRequest from './views/NewRequest/NewRequest'
import Admin from './views/Admin/Admin'
import Authentication from './views/Authentication/Authentication'
import NewAssetType from './views/NewAssetType/NewAssetType'
import NewAsset from './views/NewAsset/NewAsset'
import ChangeAssetAssignment from './views/ChangeAssetAssignment/ChangeAssetAssignment'

const App = () => {


  return (
    <BrowserRouter>
      <AuthProvider>
        <AppFrame>
          <Switch>
            <Route exact path="/"><Home/></Route>
            <Route exact path="/auth"><Authentication /></Route>
            <Route exact path="/new-asset-request"><NewRequest /></Route>

            <Route exact path="/admin"><Admin /></Route>
            <Route exact path="/admin/new-asset-type"><NewAssetType /></Route>
            <Route exact path="/admin/new-asset"><NewAsset /></Route>
            <Route exact path="/admin/change-asset-assignment"><ChangeAssetAssignment /></Route>
          </Switch>
        </AppFrame>
      </AuthProvider>
    </BrowserRouter>
  )
}

export default App;
