import React from "react";
class Welcome extends React.Component {
	render() {
	    return <h1>Hello, {this.props.name}</h1>;
	  }
	}

const element = <Welcome name="YT" />

module.exports = Welcome;
module.exports.yt = element;
