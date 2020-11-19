<template>
<div>
  <v-app>
    <!-- <h1>{{questionData}}</h1> -->
    <p v-for="data in questionData" :key='data.id'>
      <v-card light elevation="16">
        <!-- <v-card-title class="headline">考えてみよう</v-card-title> -->
        <!-- <v-card-subtitle>card subtitle</v-card-subtitle> -->
        <v-divider class="mx-3"></v-divider>
        <v-card-text class=text-center>
          <div class="body-1 mb-1">
             <h2>{{data.content}}</h2>
          </div>
        </v-card-text>
        <v-card-actions class="justify-center">
          <!-- <v-spacer></v-spacer> -->
          <v-btn large>大丈夫！</v-btn>
          <v-btn large>考え直す</v-btn>
        </v-card-actions>
      </v-card>
    </p>
  </v-app>
</div>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  props: {
    questionData: {
      type: Array
    }
  }
}
</script>
