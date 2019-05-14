<template>
  <v-app>
    <v-layout justify-center align-center column>
      <h1 class="display-4">Hello</h1>
      <h1 style="margin-top:1rem" class="headline">Welcome to fifa19 player suggestion system</h1>
      <router-link to="/position">
      <v-btn class="butt" style="margin-top:2rem" color="primary">Get started</v-btn>
      </router-link>
    </v-layout>
  </v-app>
</template>
<style>
.full {
  height: 100vh;
}
.butt:hover {
    transform: scale(1.02) translateY(-4px);
}

.butt:active {
    transform: scale(0.98) translateY(-2px);
}
</style>

