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
            <v-card-actions>
            <v-btn text v-on:click="GetTweet" id="TWEET">
              <v-icon>mdi-twitter</v-icon>
              ツイートする
            </v-btn>
            <v-btn text v-on:click="show_message">
              <v-icon>mdi-account-check-outline</v-icon>
                完了
              </v-btn>
            </v-card-actions>
            </v-alert>
          </div>
        </v-card-text>
      </v-card>
    </p>
  </v-app>
</div>
</template>

<script>
/* eslint-disable */
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
        // alert('買お\う！')
        this.index = 0
        this.status = -1
        // this.$emit('catchStatus', -1)
      }
    },
    GetTweet (str, code) {
      var textAll = this.questionData.content;
      // this.recentUrl;
      var inputData = textAll.replace(/\r?\n/g, '%0D%0A');
      var path =
        'https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text=' +
        inputData;
        target.innerHTML = '<a href=' + path + '>Tweet</a>';
      },
    show_message () {
      // this.message = "お疲れ様でした!"
      alert('お疲れ様でした！このタブは閉じても大丈夫です。')

    },
  },
  computed: {

  }
}
</script>
