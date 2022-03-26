import React from 'react';
import { useLocation } from 'react-router-dom';

import PageHeader from '../PageHeader/PageHeader';
import style from './app-frame.module.scss';

const AppFrame = ({ children }) => {
  const location = useLocation();

  return (
    <div className={style.appFrame}>
      {location.pathname !== '/' && <PageHeader />}
      {children}
    </div>
  );
};

export default AppFrame;
