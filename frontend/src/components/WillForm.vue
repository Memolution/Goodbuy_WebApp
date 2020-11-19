<template>
<div>
  <v-app>
    <v-card>
      <v-card-title>買う意思チェック</v-card-title>
      <v-card-text>
        <v-form ref="will_form">
          <v-text-field
            id="title"
            v-model="text1"
            label="Title">
          </v-text-field>

          <v-col cols="12" md="6">
            <v-textarea
              filled name="input-7-4"
              label="Will"
              >
            </v-textarea>
          </v-col>

          <v-text-field
            v-model="text3"
            label="Impression">
          </v-text-field>
        </v-form>
      </v-card-text>

      <v-divider></v-divider>
      <v-card-actions>
        <v-btn text v-on:click="submit">Send</v-btn>
        <span v-if="success">送信成功！</span>
      </v-card-actions>
    </v-card>
  </v-app>
</div>
</template>

<script>
export default {
  data () {
    return {
      text: {

      }
    }
  }
}
</script>
