<template >
  <v-app>
    <div class="eiei">
      <div class="aside">
          <v-avatar
            size="100"
            color="white"
          >
            <img :src="this.compareData[1].pic" alt="avatar">
          </v-avatar>
          <h2 class="headline">{{this.compareData[1].name}}</h2>
           <v-avatar
            size="70"
            color="white"
            style="margin-top: 2rem"
          >
            <img :src="this.compareData[1].teamLogo" alt="avatar">
          </v-avatar>
          <h2 class="headline">{{this.compareData[1].team}}</h2>
      <v-card style="margin-top: 2rem">
        <v-list>
          <v-list-tile
            v-for="item in items2"
            :key="item.title"
          >
            <v-list-tile-action>
              <v-icon v-if="item.icon" color="primary">star</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>
              <v-list-tile-title v-text="item.title"></v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-content style="margin-left: 2rem;">
              <v-list-tile-title v-text="item.value"></v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
      </div>
      <div class="middle"></div>
      <div class="aside">
          <v-avatar
            size="100"
            color="white"
          >
            <img :src="this.compareData[0].pic" alt="avatar">
          </v-avatar>
          <h2 class="headline">{{this.compareData[0].name}}</h2>
           <v-avatar
            size="70"
            color="white"
            style="margin-top: 2rem"
          >
            <img :src="this.compareData[0].teamLogo" alt="avatar">
          </v-avatar>
          <h2 class="headline">{{this.compareData[0].team}}</h2>
      <v-card style="margin-top: 2rem">
        <v-list>
          <v-list-tile
            v-for="item in items1"
            :key="item.title"
          >
            <v-list-tile-action>
              <v-icon v-if="item.icon" color="primary">star</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>
              <v-list-tile-title v-text="item.title"></v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-content style="margin-left: 2rem;">
              <v-list-tile-title v-text="item.value"></v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
      </div>
      </div>
    </div>
    <canvas id="myChart"></canvas>
  </v-app>
</template>
<script>
import Chart from 'chart.js';
import planetChartData from '../chart-data';

export default {
  data() {
    return {
      planetChartData: planetChartData,
      compareData: this.$store.state.compare_data,
      items1: [],
      items2: []
    }
  },
  methods: {
    createChart(chartId, chartData) {
      var ctx = document.getElementById('myChart');
      var myChart = new Chart(ctx, {
          type: chartData.type,
          data: chartData.data,
          options: chartData.options,
      });
    },
    compare(player1, player2) {
      let res = parseInt(player1) - parseInt(player2)
      console.log(res)
      if (res > 0) return true
      else return false
      
    },
    compareHandler() {
      let chk = false
      let tmp1 = []
      let tmp2 = []
      let useData1 = Object.keys(this.compareData[0]).slice(27, 87).reduce((result, key) => {
                      result[key] = this.compareData[0][key]
                      return result
                    }, {})
      let useData2 = Object.keys(this.compareData[1]).slice(27, 87).reduce((result, key) => {
                      result[key] = this.compareData[1][key]
                      return result
                    }, {})
      for( var key in useData1 ) {
        chk = this.compare(this.compareData[0][key], this.compareData[1][key])
        if ( chk === true ) {
          tmp1.push({
            icon: true,
            title: key,
            value: this.compareData[0][key]
          })
          tmp2.push({
            icon: false,
            title: key,
            value: this.compareData[1][key]
          })
        } else {
          tmp1.push({
            icon: false,
            title: key,
            value: this.compareData[0][key]
          })
          tmp2.push({
            icon: true,
            title: key,
            value: this.compareData[1][key]
          })
        }
      }
      this.items1 = tmp1
      this.items2 = tmp2
    }
  },
  created() {
    this.compareHandler()
  }
}
</script>
<style>
.eiei {
  display: flex;
  justify-content: space-around;
}
.middle {
  display: flex;
  flex-direction: column;
  width: 30vw;
  margin: 0 3rem 0 3rem;
}
.aside {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 35vw;
}

</style>

