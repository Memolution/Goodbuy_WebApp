<template>
  <div>
  <v-row>
    StartTime
    <v-menu
      ref="timePicker"
      v-model="showTimePicker"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
      min-width="290px"
      persistent
      :return-value.sync="startTime"
    >
      <template v-slot:activator="{ on }">
        <v-text-field
        v-model="startTime"
        prepend-icon="mdi-clock-outline"
        readonly
        v-on="on"
        ></v-text-field>
      </template>
      <v-time-picker
        v-model="startTime"
        :allowed-minutes="allowedMinutes"
        class="mt-4"
        format="24hr"
        scrollable
        min="0:00"
        max="23:59"
        @click:minute="$refs.timePicker.save(startTime)">
      </v-time-picker>
    </v-menu>
  </v-row>

  <v-row>
    EndTime
    <v-menu
      ref="timePicker"
      v-model="showTimePicker"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
      min-width="290px"
      persistent
      :return-value.sync="endTime"
    >
      <template v-slot:activator="{ on }">
        <v-text-field
        v-model="EndTime"
        prepend-icon="mdi-clock-outline"
        readonly
        v-on="on"
        ></v-text-field>
      </template>
      <v-time-picker
        v-model="endTime"
        :allowed-minutes="allowedMinutes"
        class="mt-4"
        format="24hr"
        scrollable
        min="0:00"
        max="23:59"
        @click:minute="$refs.timePicker.save(endTime)">
      </v-time-picker>
    </v-menu>
  </v-row>
</div>
</template>

<script>
export default {
  name: 'TimePicker',
  data: () => {
    return {
      // startTime: '00:00',
      // endTime: '00:00'
      // time: '11:15',
      // timeStep: '10:10'
      showTimePicker: false
    }
  },
  methods: {
    dateStartTime () {
      return this.startTime
    },
    // allowedHours: v => v % 2,
    allowedMinutes: v => v >= 0 && v <= 55
    // allowedStep: m => m % 10 === 0

  }
}
</script>
