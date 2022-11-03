import React, { useContext } from 'react';
import UsersForm from './UsersForm';
import UsersContext from '../context/UsersContext';

const AddUser = ({ history }) => {
  const { users, setUsers } = useContext(UsersContext);

  const handleOnSubmit = (user) => {
    setUsers([user, ...users]);
    history.push('/');
  };

  return (
    <React.Fragment>
      <UsersForm handleOnSubmit={handleOnSubmit} />
    </React.Fragment>
  );
};

export default AddUser;
