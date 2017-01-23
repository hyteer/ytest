//const user = "YT";
var user = { firstName: "YT", lastName: "Hoo"};
user.firstName = "Ming"

function formatName(user){
	return user.firstName + " " + user.lastName;
}


const elHello = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);

const elName = <h3>Hi { formatName(user) }</h3>;

const element = <div>
	{elHello}
	{elName}
</div>

function tick(){
	const element = <div> Time is : { new Date().toLocaleTimeString() }</div>
	ReactDOM.render(
		element,
		document.getElementById('root')
	);
}

/*
ReactDOM.render(
	element,
	document.getElementById('root')
);
*/

setInterval(tick, 1000)

