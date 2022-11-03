import React, { useContext } from 'react';
import _ from 'lodash';
import Users from './Users';
import UsersContext from '../context/UsersContext';

const UsersList = () => {
  const { users, setUsers } = useContext(UsersContext);

  const handleRemoveUser = (id) => {
    setUsers(users.filter((user) => user.id !== id));
  };

  return (
    <React.Fragment>
      <div className="user-list">
        {!_.isEmpty(users) ? (
          users.map((user) => (
            <Users key={user.id} {...user} handleRemoveUser={handleRemoveUser} />
          ))
        ) : (
          <p className="message">No users available. Please add some users.</p>
        )}
      </div>
    </React.Fragment>
  );
};

export default UsersList;
