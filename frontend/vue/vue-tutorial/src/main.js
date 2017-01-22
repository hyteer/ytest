// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// src/main.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store'
import VueResource from 'vue-resource'

import App from './App'
import Home from './components/Home'
import 'bootstrap/dist/css/bootstrap.css'

Vue.use(VueRouter)
Vue.use(VueResource)

const routes = [{
  path : '/',
  component : Home
},{
  path : '/home',
  component : Home
}];

const router = new VueRouter({
  routes
});

/* eslint-disable no-new */
// 实例化我们的 Vue
var app = new Vue({
  el: '#app',
  router,
  ...App,
});
