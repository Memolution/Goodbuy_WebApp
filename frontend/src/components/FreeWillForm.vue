<template>
  <div>
    <v-app>
        <v-card>
        <v-card-title>購入理由を自由記述で書いてみよう</v-card-title>
        <h2>記入例</h2>
        <p>原付と黄色のヘルメットを買いたいと思います。活動範囲が広くなるからです。一人で海に行ったりしたいから、買います。車は、高いしお金がかかるので、原付にしました。二人乗りは、免許を取り直す必要があり、少しだるい。だから原付。</p>
        <v-textarea outlined rows="10" name="input-7-4" v-model="tweetContent.tweetWhy" label="購買動機を入力してね"></v-textarea>
        <v-text-field
          v-model="recentUrl"
          label="商品のURLを入力してね"
        >
        </v-text-field>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn text v-on:click="GetTweet" id="TWEET">
            <v-icon>mdi-twitter</v-icon>
            ツイートする
          </v-btn>
          <!-- <span v-if="success">送信成功！</span> -->
        </v-card-actions>
      </v-card>
      <div>
        {{validation.validateResult}}
      </div>
    </v-app>
  </div>

</template>

<script>
export default {
  name: 'willForm',
  data: function () {
    return {
      tweetContent: {
        tweetWhy: ''
      },
      validation: {
        validateResult: ''
      },
      recentUrl: []
    }
  },
  methods: {
    GetTweet (str, code) {
      if (this.tweetContent.tweetWhy.length < 20) {
        this.validation.validateResult = '20字以上入力してください'
      } else if (this.tweetContent.tweetWhy.length > 87) {
        this.validation.validateResult = '熱入りすぎだよ！'
      } else {
        this.validation.validateResult = 'めっちゃいい理由！'
        var target = document.getElementById('TWEET')
        var textAll = this.tweetContent.tweetWhy + this.recentUrl
        var inputData = textAll.replace(/\r?\n/g, '%0D%0A')
        var path = 'https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text=' + inputData
        target.innerHTML = '<a href=' + path + '>Tweet</a>'
      }
    }
  }
}
</script>

<style lang="scss">
.tweetBox {
  border: 2px solid #00aced ;
  border-radius: 0.67em;
  padding: 0.5em;
  background-color: snow;
  width: 50em;
  height: 15px;
  font-size: 1em;
  line-height: 1.2;
}
#TWEET {
  width:150px;
  height:30px;
  line-height:30px;
  text-align:center;

  background-color: #55acee;
  border: 2px solid #55acee;
  border-radius: 20px;
  color: #fff;
  padding:4px 32px;
  -webkit-transition: all .3s;
  transition: all .3s;
}
#TWEET:hover {
  background-color: #fff;
  color: #55acee;
}
.error { color: red; }
</style>
