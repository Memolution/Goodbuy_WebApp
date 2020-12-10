<template>
<div>
  <v-app>
    <p v-if="this.status == 0">
      <v-card light elevation="16">
        <v-divider class="mx-3"></v-divider>
        <v-card-text class=text-center>
          <div class="body-1 mb-1">
             <h2>{{questionData[index].content}}</h2>
          </div>
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn large @click="nextQuersiton">大丈夫！</v-btn>
          <v-btn large @click="breakPoint">考え直す</v-btn>
        </v-card-actions>
      </v-card>
    </p>

    <p v-else-if="this.status == 1">
      <v-card light elevation="16">
        <v-divider class="mx-3"></v-divider>
        <v-card-text class=text-center>
          <div class="body-1 mb-1">
            <v-alert
            outlined
            type="warning"
            prominent
            border="left"
            >
               <h2>
                 買いたい商品を思い浮かべながらもう少し考えてみよう
               </h2>
             </v-alert>
          </div>
        </v-card-text>
        <p v-for="data in questionData" :key='data.id'>
            <v-card light elevation="16">
              <v-divider class="mx-3"></v-divider>
              <v-card-text class=text-center>
                <div class="body-1 mb-1">
                   <h2>{{data.content}}</h2>
                </div>
              </v-card-text>
            </v-card>
          </p>
      </v-card>
    </p>

    <p v-else-if="this.status == -1">
      <v-card light elevation="16">
        <v-divider class="mx-3"></v-divider>
        <v-card-text class=text-center>
          <div class="body-1 mb-1">
            <v-alert
            outlined
            type="success"
            prominent
            border="left"
            >
            <h2>買おう！</h2>
            </v-alert>
          </div>
        </v-card-text>
      </v-card>
    </p>
  </v-app>
</div>
</template>

<script>
export default {
  data () {
    return {
      // status: 0,
      index: 0
    }
  },
  props: {
    questionData: {
      type: Array
    },
    status: {

    }
  },
  methods: {
    breakPoint () {
      // alert('もう少し考えてからまた来てね')
      this.index = 0
      this.status = 1
      // this.$emit('catchStatus', 1)
    },
    nextQuersiton () {
      if (this.index < this.questionData.length - 1) {
        // console.log(this.index)
        this.index += 1
      } else {
        // alert('買おう！')
        this.index = 0
        this.status = -1
        // this.$emit('catchStatus', -1)
      }
    }
  },
  computed: {

  }
}
</script>
