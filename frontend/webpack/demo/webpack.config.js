module.exports = {
    entry: ['./app.js'],
    output: {
        path: './', // 输出文件的保存路径
        filename: 'bundle.js' // 输出文件的名称
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

}
