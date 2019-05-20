<template>
    <v-app>
    <div v-if="load">
    <v-layout style="margin-top: 30vh;" align-center column>
        <h1 class="display-4">Property</h1>
        <h1 style="margin-top:2rem; margin-bottom:2rem;" class="headline">Add player property you are looking for</h1>
        <label>Range 0-100</label>
      <div v-for="(data, index) in $store.state.properties_input" :key="index">
        <v-layout row wrap align-baseline justify-center>
          <v-flex xs2>
              <v-select
                :items="proper"
                label="Property"
                v-model="data.name"
                solo
              ></v-select>
          </v-flex>
          <v-flex xs7>
            <v-slider
              v-model="data.value"
              class="align-center"
              label="Value"
              :max="max"
              :min="min"
              hide-details
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
          <v-btn @click="deleteProp(data)" color="error">Delete</v-btn>
        </v-layout>
      </div>
        <v-btn @click="addProp" color="success">Add</v-btn>
    </v-layout>
    <v-container>
      <v-layout justify-space-between>
          <router-link to="/position">
            <v-btn class="butt" style="margin-top:2rem" color="primary">Previous</v-btn>
          </router-link>
          <router-link to="/result">
            <v-btn @click="submit" class="butt" style="margin-top:2rem" color="primary">Submit</v-btn>
          </router-link>
        </v-layout>
    </v-container>
    </div>
    <div v-else>
    <v-layout style="margin-top: 30vh;" align-center column>
      <v-responsive color="primary" dark>
            <v-container fill-height>
            <v-layout align-center>
                <v-flex text-xs-center>
                <h3 class="display-3">
                Calculating
                <v-progress-circular
                indeterminate
                color="black"
                ></v-progress-circular>
                </h3>
                </v-flex>
            </v-layout>
            </v-container>
      </v-responsive>
    </v-layout>
    </div>
    </v-app>
</template>
<script>
import { mapActions } from 'vuex'
import { properties } from '../enum'


export default {
  data() {
    return {
      proper: properties,
      min: 0,
      max: 100,
      load: true,
    }
  },
  methods: {
    ...mapActions([
      'addProp',
      'deleteProp'
    ]),
    submit() {
      this.load = false;
    }
  },
}
</script>