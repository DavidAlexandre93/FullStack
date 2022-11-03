import React, { useContext } from 'react';
import UsersForm from './UsersForm';
import { useParams } from 'react-router-dom';
import UsersContext from '../context/UsersContext';

const EditUser = ({ history }) => {
  const { users, setUsers } = useContext(UsersContext);
  const { id } = useParams();
  const userToEdit = users.find((user) => user.id === id);

  const handleOnSubmit = (user) => {
    const filteredUsers = users.filter((user) => user.id !== id);
    setUsers([user, ...filteredUsers]);
    history.push('/');
  };

  return (
    <div>
      <UsersForm user={userToEdit} handleOnSubmit={handleOnSubmit} />
    </div>
  );
};

export default EditUser;
