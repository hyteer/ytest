'use strict';

function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

var user = {
  firstName: 'Tony',
  lastName: 'Hoo'
};

var element = React.createElement(
  'h1',
  null,
  'Hello, ',
  formatName(user),
  '!'
);

const el = <h3>Hi { formatName(user) } !</h3>;

ReactDOM.render(
	el, 
	document.getElementById('root')
	);