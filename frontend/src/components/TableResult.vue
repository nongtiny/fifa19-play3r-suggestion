<template>
  <v-app>
    <v-container>
        <v-card>
            <v-card-title>
                <p class="font-weight-medium">Your results</p>
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="search"
                    label="Search"
                    single-line
                    hide-details
                ></v-text-field>
            </v-card-title>
            <v-data-table
            v-model="selected"
            :headers="headers"
            :items="selectedRes"
            :search="search"
            :expand="expand"
            :disable-initial-sort=true
            item-key="name"
            
            default-sort="Overall:desc"
            >
            <template v-slot:no-data>
                <v-alert :value="true" color="error" icon="warning">
                    Sorry, nothing to display here :(
                </v-alert>
            </template>
            <template v-slot:items="props">
                <tr>
                    <td v-on:click="props.selected = !props.selected; selectHandler">
                    <v-checkbox
                        :input-value="props.selected"
                        primary
                        hide-details
                    ></v-checkbox>
                    </td>
                    <td class="see-detail" v-on:click="props.expanded = !props.expanded">
                        <img :src="props.item.pic"/>
                        {{props.item.name}}
                    </td>
                    <td class="text-xs-center">{{ props.item.overall }}</td>
                    <td class="text-xs-center">{{ props.item.potential }}</td>
                    <td class="text-xs-center">${{ props.item.value }}</td>
                    <td class="text-xs-center">{{ props.item.simValue }}</td>
                </tr>
            </template>
            <template v-slot:no-results>
                <v-alert :value="true" color="error" icon="warning">
                Your search for "{{ search }}" found no results.
                </v-alert>
            </template>
            <template v-slot:expand="props">
            <v-card class="player-details" flat>
                <div class="box">
                    <h1>Position</h1>
                    <p>{{props.item.position}}</p>
                </div>
                <div class="box">
                    <h1>Age</h1>
                    <p>{{props.item.age}}</p>
                </div>
                <div class="box">
                    <h1>Nationality</h1>
                    <p class="team">
                        <img style="margin-right:0.5rem" :src="props.item.flag"/>
                        {{props.item.nationality}}
                    </p>
                </div>
                <div class="box">
                    <h1>Team</h1>
                    <p class="team">
                        <img style="margin-right:0.5rem" :src="props.item.teamLogo"/>
                        {{props.item.team}}
                    </p>
                </div>
                <div class="box">
                    <h1>Jersey Number</h1>
                    <p>{{props.item.jerseyNum}}</p>
                </div>
                <div class="box">
                    <h1>Wage</h1>
                    <p>${{props.item.wage}}</p>
                </div>
                <div class="box">
                    <h1>Special</h1>
                    <p>{{props.item.special}}</p>
                </div>
                <div class="box">
                    <h1>Preferred Foot</h1>
                    <p>{{props.item.preferFoot}}</p>
                </div>
                <div class="box">
                    <h1>Skill Move</h1>
                    <p>{{props.item.skillMove}} out of 5</p>
                </div>
                <div class="box">
                    <h1>Body Type</h1>
                    <p>{{props.item.bodyType}}</p>
                </div>
                <div class="box">
                    <h1>Height</h1>
                    <p>{{props.item.height}} cm</p>
                </div>
                <div class="box">
                    <h1>Weight</h1>
                    <p>{{props.item.weight}} kg</p>
                </div>
            </v-card>
            </template>
            </v-data-table>
        </v-card>
    </v-container>
    <div v-if="this.selected.length != 0" transition="slide-y-reverse-transition">
        <div class="compare">
            <div v-for="(item, index) in this.selected" :key="index">
                <v-chip>
                    <v-avatar>
                    <img :src="item.pic" alt="trevor">
                    </v-avatar>
                    {{item.name}}
                </v-chip>
            </div>
        </div>
        <router-link to="/compare">
            <v-btn @click="compare" class="butt" color="primary">Compare</v-btn>
        </router-link>
    </div>
  </v-app>
</template>
<script>
export default {
    data () {
        return {
            table_row: this.$store.state.result_data,
            search: '',
            headers: [
                {
                text: '',
                sortable: false,
                value: 'name'
                },
                { text: 'Player', align: 'center', sortable: false,},
                { text: 'Overall', align: 'center', value: 'overall' },
                { text: 'Potential', align: 'center', value: 'potential' },
                { text: 'Value', align: 'center', value: 'value' },
                { text: 'Similarity value', align: 'center', value: 'simValue' }

            ],
            selectedRes: [],
            playerDetail: null,
            selected: [],
        }
    },
    methods: {
        compare() {
            this.$store.state.compare_data = this.selected;
        },
        setup() {
            console.log('calculating');
            const simiData = this.$store.getters.posNotNull.concat(this.$store.getters.propNotNull)
            fetch(`http://localhost:5000/api/data`,{
                method: 'POST',
                mode: 'cors', 
                cache: 'no-cache', 
                credentials: 'same-origin', 
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(simiData), // body data type must match "Content-Type" header
                })
                .then(response => response.text()).then(
                text => {
                    let data = JSON.parse(text)
                    console.log(data)
                    this.table_row = data.tdata
                }
                )
                .catch(function(err) {
                console.log('Fetch Error :-S', err);
                });
            setTimeout(this.setData(), 6000)
        },
        setData() {
            let table_item = []
            this.$store.state.result_data.forEach(element => {
                table_item.push({
                    id: element[0],
                    name: element[1],
                    age: element[2],
                    pic: element[3],
                    nationality: element[4],
                    flag: element[5],
                    overall: element[6],
                    potential: element[7],
                    team: element[8],
                    teamLogo: element[9],
                    value: element[10],
                    wage: element[11],
                    special: element[12],
                    preferFoot: element[13],
                    interRepute: element[14],
                    weakFoot: element[15],
                    skillMove: element[16],
                    workRate: element[17],
                    bodyType: element[18],
                    position: element[20],
                    jerseyNum: element[21],
                    joined: element[22],
                    loanedFrom: element[23],
                    contractValid: element[24],
                    height: element[25],
                    weight: element[26],
                    LS: element[27],
                    ST: element[28],
                    RS: element[29],
                    LW: element[30],
                    LF: element[31],
                    CF: element[32],
                    RF: element[33],
                    RW: element[34],
                    LAM: element[35],
                    CAM: element[36],
                    RAM: element[37],
                    LM: element[38],
                    LCM: element[39],
                    CM: element[40],
                    RCM: element[41],
                    RM: element[42],
                    LWB: element[43],
                    LDM: element[44],
                    CDM: element[45],
                    RDM: element[46],
                    RWB: element[47],
                    LB: element[48],
                    LCB: element[49],
                    CB: element[50],
                    RCB: element[51],
                    RB: element[52],
                    Crossing: element[53],
                    Finishing: element[54],
                    HeadingAccuracy: element[55], 
                    ShortPassing: element[56], 
                    Volleys: element[57], 
                    Dribbling: element[58],
                    Curve: element[59], 
                    FKAccuracy: element[60], 
                    LongPassing: element[61], 
                    BallControl: element[62], 
                    Acceleration: element[63], 
                    SprintSpeed: element[64], 
                    Agility: element[65], 
                    Reactions: element[66], 
                    Balance: element[67], 
                    ShotPower: element[68], 
                    Jumping: element[69], 
                    Stamina: element[70], 
                    Strength: element[71], 
                    LongShots: element[72], 
                    Aggression: element[73], 
                    Interceptions: element[74], 
                    Positioning: element[75], 
                    Vision: element[76], 
                    Penalties: element[77], 
                    Composure: element[78], 
                    Marking: element[79], 
                    StandingTackle: element[80],
                    SlidingTackle: element[81],
                    GKDiving: element[82], 
                    GKHandling: element[83],
                    GKKicking: element[84],
                    GKPositioning: element[85],
                    GKReflexes: element[86], 
                    Release: element[87],
                    simValue: element[88]
                })
            });
            this.selectedRes = table_item
        },
    },
    computed: {
        selectHandler() {
            if (this.selected.length > 2) {
                this.selected.shift()
            }
        }
    },
    created() {
        this.setup()
    }
}
 
// table_column: ['ID', 'Name', 'Age', 'Photo',
//             'Nationality', 'Flag', 'Overall', 'Potential',
//             'Club', 'Club Logo', 'Value', 'Wage', 'Special',
//             'Preferred Foot', 'International Reputation',
//             'Weak Foot', 'Skill Moves', 'Work Rate',
//             'Body Type', 'Real Face', 'Position', 'Jersey Number',
//             'Joined', 'Loaned From', 'Contract Valid Until',
//             'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF',
//             'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM',
//             'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB',
//             'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing', 'Finishing',
//             'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
//             'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 
//             'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 
//             'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 
//             'LongShots', 'Aggression', 'Interceptions', 'Positioning', 
//             'Vision', 'Penalties', 'Composure', 'Marking', 
//             'StandingTackle', 'SlidingTackle', 'GKDiving', 
//             'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 
//             'Release Clause', 'Similarity'],
</script>
<style>
.player-details {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  background-color: #ddd;
  color: #555;
}
.player-details .box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    width: 300px;
    box-shadow: -1px 10px 11px -10px rgba(0,0,0,0.3);
    margin: 0.5rem;
}
.player-details .box h1{
    position: relative;
    top:3px;
    font-size: 1rem;
    font-weight: 800;
    color: #222;
}
.player-details .box p{
    margin-top: 2rem;
}
.player-details .box .team {
    display: flex;
    justify-content: baseline;
    align-items: center;
}

.see-detail {
    display: flex;
    align-items: center;
    justify-content: space-around;
}

.see-detail:hover {
    cursor: pointer;
    font-weight: 700; 
}
.check {
  border: 1px solid #000;
}

.compare {
    display: flex;
    align-items: center;
    width: 100vw;
    height: 60px;
    background-color: #ccc;
    position: fixed;
    bottom: 0%;
}

.butt {
   float: right;
   margin-bottom: 0.75rem;
}
</style>
