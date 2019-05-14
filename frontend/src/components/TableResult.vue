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
        :headers="headers"
        :items="selectedRes"
        :search="search"
        :expand="expand"
        :disable-initial-sort=true
        item-key="name"
        
        default-sort="Overall:desc"
        >
        <template v-slot:items="props">
            <tr @click="props.expanded = !props.expanded">
                <td>{{props.item.name}}</td>
                <td class="text-xs-center">{{ props.item.overall }}</td>
                <td class="text-xs-center">{{ props.item.potential }}</td>
                <td class="text-xs-center">{{ props.item.value }}</td>
                <td class="text-xs-center">{{ props.item.position }}</td>
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
                <h1>Photo</h1>
                <p><img :src="props.item.player.pic"/></p>
            </div>
             <div class="box">
                <h1>Age</h1>
                <p>{{props.item.player.age}}</p>
            </div>
            <div class="box">
                <h1>Nationality</h1>
                <p>{{props.item.player.nationality}}</p>
            </div>
             <div class="box">
                <h1>Team</h1>
                <p class="team">
                    <img style="margin-right:0.5rem" :src="props.item.player.teamLogo"/>
                    {{props.item.player.team}}
                </p>
            </div>
        </v-card>
        </template>
        </v-data-table>
    </v-card>
    </v-container>
  </v-app>
</template>
<script>
export default {
    data () {
        return {
            table_column: ['ID', 'Name', 'Age', 'Photo',
            'Nationality', 'Flag', 'Overall', 'Potential',
            'Club', 'Club Logo', 'Value', 'Wage', 'Special',
            'Preferred Foot', 'International Reputation',
            'Weak Foot', 'Skill Moves', 'Work Rate',
            'Body Type', 'Real Face', 'Position', 'Jersey Number',
            'Joined', 'Loaned From', 'Contract Valid Until',
            'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF',
            'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM',
            'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB',
            'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing', 'Finishing',
            'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
            'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 
            'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 
            'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 
            'LongShots', 'Aggression', 'Interceptions', 'Positioning', 
            'Vision', 'Penalties', 'Composure', 'Marking', 
            'StandingTackle', 'SlidingTackle', 'GKDiving', 
            'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 
            'Release Clause', 'Similarity'],
            table_row: this.$store.state.result_data,
            search: '',
            headers: [
                {
                text: 'Player',
                align: 'left',
                sortable: false,
                value: 'name'
                },
                { text: 'Overall', align: 'center', value: 'overall'},
                { text: 'Potential', align: 'center', value: 'potential' },
                { text: 'Value', align: 'center', value: 'value' },
                { text: 'Position', align: 'center', value: 'position' },
                { text: 'Similarity value', align: 'center', value: 'simValue' }
            ],
            selectedRes: null,
            playerDetail: null,
        }
    },
    methods: {
        setData() {
            let table_item = []
            this.table_row.forEach(element => {
                table_item.push({
                    player:  {
                        age: element[2],
                        pic: element[3],
                        nationality: element[4],
                        team: element[8],
                        teamLogo: element[9]
                    },
                    name: element[1],
                    overall: element[6],
                    potential: element[7],
                    value: element[10],
                    position: element[20],
                    simValue: element[88]
                })
            });
            this.selectedRes = table_item
        }
    },
    created() {
        this.setData()
    },
}
 
</script>
<style>
.player-details {
  display: flex;
  background-color: #ddd;
  color: #555;
}
.player-details .box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    width: 100%;
}
.player-details .box h1{
    position: absolute;
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
.check {
  border: 1px solid #000;
}
</style>
