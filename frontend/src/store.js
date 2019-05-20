import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
const state = {
  properties_input: [],
  positions_input: [],
  result_data: [],
  compare_data: []
}

const mutations = {
  ADD_PROP (state) {
    state.properties_input.push({
      name: null,
      value: null
    })
  },
  ADD_POS (state) {
    state.positions_input.push({
      name: null,
      value: null
    })
  },
  UPDATE_PROP(state, prop, prop_input) {
    let props = state.properties_input
    props[props.indexOf(prop)] = prop_input
  },
  UPDATE_POS_NAME(state, pos, pos_input_name) {
    let poss = state.positions_input
    poss[poss.indexOf(pos)].name = pos_input_name
  },
  UPDATE_POS_VALUE(state, pos, pos_input_value) {
    let poss = state.positions_input
    poss[poss.indexOf(pos)].name = pos_input_value
  },
  DELETE_PROP (state, prop) {
    let props = state.properties_input
    props.splice(props.indexOf(prop), 1)
  },
  DELETE_POS (state, pos) {
    let poss = state.positions_input
    poss.splice(poss.indexOf(pos), 1)
  }
}
const actions = {
  addProp: ({commit}) => commit('ADD_PROP'),
  addPos: ({commit}) => commit('ADD_POS'),
  updateProp: ({commit}) => commit('UPDATE_PROP', prop),
  updatePos: ({commit}) => commit('UPDATE_POS', pos),
  deleteProp: ({commit}, prop) => commit('DELETE_PROP', prop),
  deletePos: ({commit}, pos) => commit('DELETE_POS', pos),
}
const getters = {
  propNotNull: state => state.properties_input.filter(x => x.name !== null && x.name !== '' && x.value !== null && x.value !== ''),
  posNotNull: state => state.positions_input.filter(x => x.name !== null && x.name !== '' && x.value !== null && x.value !== '')
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})