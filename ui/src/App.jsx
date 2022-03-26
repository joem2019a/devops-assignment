import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import AppFrame from './components/AppFrame/AppFrame';
import Home from './views/Home/Home'
import NewRequest from './views/NewRequest/NewRequest'

const App = () => {

  return (
    <BrowserRouter>
      <AppFrame>
        <Switch>
          <Route exact path="/"><Home/></Route>
          <Route exact path="/new-asset-request"><NewRequest /></Route>
        </Switch>
      </AppFrame>
    </BrowserRouter>
  )
}

export default App;
