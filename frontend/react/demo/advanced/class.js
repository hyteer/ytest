class Welcome extends React.Component {
	render() {
	    return <h1>Hello, {this.props.name}</h1>;
	  }
	}

const element = <Welcome name="Silly" />

React.render(
	element,
	document.getElementById('root')
	)
