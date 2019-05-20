import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/about', component: 'About' },
  { path: '/result', 
    component: 'TableResult',
    beforeEnter: (to, from, next)=>{
      console.log('calculating');
      fetch(`http://localhost:5000/api/data`,{
      method: 'POST',
      mode: 'cors', 
      cache: 'no-cache', 
      credentials: 'same-origin', 
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(store.getters.posNotNull.concat(store.getters.propNotNull)), // body data type must match "Content-Type" header
      })
      .then(response => response.text()).then(
      text => {
          let data = JSON.parse(text)
          store.state.result_data = data.tdata
          console.log(data)
          next()
      })
      .catch(function(err) {
          console.log('Fetch Error :-S', err);
      });
    } 
  },
  { path: '/compare', component: 'ComparePlayer' },
  { path: '/position', component: 'PositionInput' },
  { path: '/property', component: 'PropertyInput' },
  { path: '*', component: 'NotFound' }
]
// beforeRouteEnter (to, from, next) {
  
// },
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
