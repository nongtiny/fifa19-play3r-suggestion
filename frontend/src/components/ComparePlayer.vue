<template >
  <v-app>
    <div class="eiei">
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
          <h2 class="subheading" style="margin-top: 2rem"><strong>Height</strong> {{parseInt(this.compareData[0].height)}}</h2>
          <h2 class="subheading" style="margin-top: 2rem"><strong>Weight</strong> {{parseInt(this.compareData[0].weight)}}</h2>
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
      <div class="middle">
        <canvas id="myChart" width="550" height="550"></canvas>
        <canvas style="margin-top:5rem" id="myChart2" width="550" height="550"></canvas>
      </div>
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
          <h2 class="subheading" style="margin-top: 2rem"><strong>Height</strong> {{parseInt(this.compareData[1].height)}}</h2>
          <h2 class="subheading" style="margin-top: 2rem"><strong>Weight</strong> {{parseInt(this.compareData[1].weight)}}</h2>
          
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
    </div>
  </v-app>
</template>
<script>
import Chart from 'chart.js';
import store from '../store'

export default {
  data() {
    return {
      compareData: store.state.compare_data,
      name1: '',
      name2: '',
      items1: [],
      items2: [],
      posiItemsLabel: [],
      posiItemsData1: [],
      posiItemsData2: [],

      propItemsLabel: [],
      propItemsData1: [],
      propItemsData2: [],
      positionChartData: {
        labels: [],
        datasets: []
      },
      propertyChartData: {
        labels: [],
        datasets: []
      }
    }
  },
  methods: {
    createChart(chartData) {
      var ctx = document.getElementById('myChart')
      var myChart = new Chart(ctx, {
          type: 'radar',
          data: chartData,
          options: {
            responsive: true,
            lineTension: 1,
          }
      })
    },
    createChart2(chartData) {
      var ctx2 = document.getElementById('myChart2')
      var myChart = new Chart(ctx2, {
          type: 'radar',
          data: chartData,
          options: {
            responsive: true,
            lineTension: 1,
          }
      })
    },
    compare(player1, player2) {
      let res = parseInt(player1) - parseInt(player2)
      if (res > 0) return true
      else return false
      
    },
    compareHandler() {
      let chk = false
      let tmp1 = []
      let tmp2 = []
      let useData1 = Object.keys(this.compareData[0]).slice(27, 86).reduce((result, key) => {
                      result[key] = this.compareData[0][key]
                      return result
                    }, {})
      let useData2 = Object.keys(this.compareData[1]).slice(27, 86).reduce((result, key) => {
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
      this.items1.forEach((el, index) => {
        if(index < 25){
          this.posiItemsLabel.push(el.title)
          this.posiItemsData1.push(parseInt(el.value))
        } else {
          this.propItemsLabel.push(el.title)
          this.propItemsData1.push(el.value)
        }
      })
      this.items2.forEach((el, index) => {
        if(index < 25){
          this.posiItemsData2.push(parseInt(el.value))
        } else {
          this.propItemsData2.push(el.value)
        }
      })
      this.positionChartData.labels = this.posiItemsLabel
      this.positionChartData.datasets.push(
        { 
          label: store.state.compare_data[0].name,
          data: this.posiItemsData1,
          backgroundColor: 'rgba(54,73,93,.5)', // Blue
          borderColor: '#36495d',
          borderWidth: 3
        },
        { // another radar graph
          label: store.state.compare_data[1].name,
          data: this.posiItemsData2,
          backgroundColor: 'rgba(71, 183,132,.5)', // Green
          borderColor: '#47b784',
          borderWidth: 3
        })
      this.propertyChartData.labels = this.propItemsLabel
      this.propertyChartData.datasets.push(
        { 
          label: store.state.compare_data[0].name,
          data: this.propItemsData1,
          backgroundColor: 'rgba(54,73,93,.5)', // Blue
          borderColor: '#36495d',
          borderWidth: 3
        },
        { // another radar graph
          label: store.state.compare_data[1].name,
          data: this.propItemsData2,
          backgroundColor: 'rgba(71, 183,132,.5)', // Green
          borderColor: '#47b784',
          borderWidth: 3
        })
      this.createChart(this.positionChartData)
      this.createChart2(this.propertyChartData)
    }
  },
  mounted() {
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

