import Vue from 'vue';

import App from './App.vue';
import input from './input.vue';

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount(`#app`);

new Vue({
  render: h => h(input),
}).$mount(`#input`);
