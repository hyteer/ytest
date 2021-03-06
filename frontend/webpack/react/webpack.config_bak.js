module.exports = {
  entry:[
    './app/main.js'
  ],
  output: {
    path: __dirname + '/assets/',
    publicPath: "/assets/",
    filename: 'bundle.js'
  },
  module: {
    loaders: [
       {
         test: [/\.js$/, /\.es6$/],
         exclude: /node_modules/,
         loader: 'babel-loader',
         query: {
           presets: ['react', 'es2015']
         }
       }
     ]
  },
  resolve: {
    extensions: ['', '.js', '.es6']
  },
  //watch: true,
};
