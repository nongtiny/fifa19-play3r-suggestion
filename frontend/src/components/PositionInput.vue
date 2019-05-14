<template>
    <v-app>
      <v-layout style="margin-top: 30vh;" align-center column>
        <h1 class="display-4">Position</h1>
        <h1 style="margin-top:2rem; margin-bottom:2rem;" class="headline">Add player position you are looking for</h1>
        <label>Range 0-100</label>
        <div v-for="(data, index) in $store.state.positions_input" :key="index">
          <v-layout row align-baseline justify-space-around>
            <v-flex xs2>
                <v-select
                  :items="poss"
                  label="Position"
                  v-model="data.name"
                  solo
                ></v-select>
            </v-flex>
            <v-flex xs6>
              <v-slider
                v-model="data.value"
                class="align-center"
                label="Value"
                :max="max"
                :min="min"
              >
                <template #append>
                  <v-text-field
                    v-model="data.value"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 60px"
                  ></v-text-field>
              </template>
              </v-slider>
            </v-flex>
            <v-btn @click="deletePos(data)" color="error">Delete</v-btn>
          </v-layout>
        </div>
        <v-btn @click="addPos" color="success">Add</v-btn>
    </v-layout>
    <v-container>
      <v-layout justify-space-between>
          <router-link to="/">
            <v-btn class="butt" style="margin-top:2rem" color="primary">Previous</v-btn>
          </router-link>
          <router-link to="/property">
            <v-btn class="butt" style="margin-top:2rem" color="primary">Next</v-btn>
          </router-link>
        </v-layout>
    </v-container>
  </v-app>
</template>
<script>
import { mapActions } from 'vuex'
import { positions } from '../enum'

export default {
  data() {
    return {
      poss: positions,
      min: 0,
      max: 100,
    }
  },
  methods: 
    mapActions([
      'addPos',
      'deletePos'
    ])
}
</script>
<style>
.butt:hover {
    transform: scale(1.02) translateY(-4px);
}

.butt:active {
    transform: scale(0.98) translateY(-2px);
}
</style>

