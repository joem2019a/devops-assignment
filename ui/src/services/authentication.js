import { createContext, useEffect, useState, useContext, useMemo } from 'react';
import { useHistory } from 'react-router-dom';

import axios from 'axios';
import useCookie from 'react-use-cookie';
import jwtDecode from 'jwt-decode';
import { pick } from 'lodash';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {

  const history = useHistory();
  const [initialLoadComplete, setInitialLoadComplete] = useState(false);
  const [token, setToken] = useCookie('token', 'null');
  const [currentUser, setCurrentUser] = useState(undefined);

  const loggedIn = useMemo(() => currentUser !== undefined, [currentUser]);

  const tokenChange = async (token) => {
    if (token === 'null') {
      history.replace('/auth');
    } else {
      try {
        if (axios.defaults.headers.common.hasOwnProperty('Authorization'))
          delete axios.defaults.headers.common['Authorization'];

        let newToken = token;
        const { exp } = jwtDecode(token);
        if (Date.now() >= exp * 1000) {
          const { data: { access_token: refreshedToken } } = await axios.get('/auth/refresh', {
            headers: {
              'Authorization': `Bearer ${token}`,
            }
          });
          newToken = refreshedToken;
        }
        const jwtData = jwtDecode(token);
        setToken(newToken);
        axios.defaults.headers.common['Authorization'] = `Bearer ${newToken}`;
        setCurrentUser(pick(
          jwtData,
          'id',
          'username',
          'email',
          'name',
          'isAdmin',
        ));
      } catch (e) {
        console.error(e);
      }
    }
  }

  useEffect(() => {
    tokenChange(token);
    setInitialLoadComplete(true);
  }, []); // eslint-disable-line

  return (
    <AuthContext.Provider 
      value={{
        currentUser,
        tokenChange,
        loggedIn,
      }}
    >
      {initialLoadComplete && children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const context = useContext(AuthContext);
  return context;
}

export default AuthProvider;
