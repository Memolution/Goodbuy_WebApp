<template>
  <div>
  <v-btn bottom color="pink" dark fab fixed right @click="dialog = !dialog">
    <v-icon>add</v-icon>
  </v-btn>
  <v-dialog v-model="dialog" width="800px">
    <v-card>
      <v-card-title class="grey darken-2">
        Create Schedule
      </v-card-title>
      <v-container grid-list-sm>
        <v-layout row wrap>
          <v-flex xs12 align-center justify-space-between>
            <v-layout align-center>
              <v-avatar size="40px" class="mr-3">
                <!-- <img
          src="//ssl.gstatic.com/s2/oz/images/sge/grey_silhouette.png"
          alt=""
          > -->
              </v-avatar>
              <v-text-field placeholder="Title">
              </v-text-field>
            </v-layout>
          </v-flex>
          <v-flex xs6>
            <v-text-field placeholder="Category">
            </v-text-field>
          </v-flex>
          <v-flex xs6>
            <v-text-field placeholder="with Whome">
            </v-text-field>
          </v-flex>
          <v-flex xs12>
            <v-row>
                <DatePicker />
            </v-row>
          </v-flex>
          <v-flex xs12>
            <v-row>
                <TimePicker />
            </v-row>
          </v-flex>
          <v-flex xs12>
            <v-row>
                <Datetime
                    v-model="requestDate"
                    :minute-interval="30"
                    :format="'YYYY-MM-DD HH:mm'"
                    :disabled-hours="['00', '01', '02', '03', '04', '05', '06', '07', '08', '17', '18', '19', '20', '21', '22', '23']"
                    :overlay="true"
                    :min-date="start"
                    :max-date="end"
                ></Datetime>
            </v-row>
          </v-flex>
          <v-flex xs12>
            <v-text-field placeholder="Notes"></v-text-field>
          </v-flex>
        </v-layout>
      </v-container>
      <v-card-actions>
        <v-btn text color="primary">
          More
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="dialog = false">
          Cancel
        </v-btn>
        <v-btn text @click="dialog = false">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
// @ is an alias to /src
import DatePicker from '@/components/DatePicker.vue'
import TimePicker from '@/components/TimePicker.vue'
import moment from 'moment'
import Datetime from 'vue-ctk-date-time-picker'
// import '../../vue-ctk-date-time-picker.css';
export default {
  name: 'TodoButton',
  data: () => ({
    requestDate: '',
    dialog: false
  }),
  components: {
    DatePicker,
    TimePicker,
    Datetime
  },
  computed: {
    start () {
      // min-date に明日の9時を指定
      const start = moment().add(1, 'days').hour(8)
      return start.format('YYYY-MM-DDTHH:mm:ss')
    },
    end () {
      // max-date に min-date から3ヶ月後を指定
      const start = moment(this.start)
      const end = start.add(3, 'months').endOf('day')
      return end.format('YYYY-MM-DDTHH:mm:ss')
    }
  }
}
</script>
