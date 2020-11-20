<template>
  <div>
    <v-app>
      <v-card>
        <v-card-title>購入理由をエレベーターピッチ風に買いてみよう</v-card-title>
        <v-card-text>

          <br />
          <h3>{{evp_template.temp1}}</h3>

          <v-text-field
            v-model="tweetContent.tweetWhy"
            label="購買動機を入力してね"
            >
          </v-text-field>

          <h3>{{evp_template.temp2}}</h3>
          <br />
          <h3>{{evp_template.temp3}}</h3>

          <v-text-field
          v-model="tweetContent.tweetWhat"
          label="どんな問題が解決できるか入力してね"
          >
          </v-text-field>

          <br />
          <h3>{{evp_template.temp4}}</h3>
          <v-text-field
            v-model="tweetContent.tweetHow"
            label="どのようにして解決できそうか入力してね"
          >
          </v-text-field>

          <br />
          <h3>{{evp_template.temp5}}</h3>
        </v-card-text>
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
      evp_template: {
        temp1: 'この商品は、',
        temp2: 'を解決する事を目的に買います。',
        temp3: 'これがあると',
        temp4: 'を',
        temp5: 'して問題を解決できます。',
        temp6: 'これは、今の私の所持品では代替',
        temp7: '。'
      },
      tweetContent: {
        tweetWhy: '',
        tweetWhat: '',
        tweetHow: ''
      },
      validation: {
        validateResult: ''
      }

    }
  },
  methods: {
    GetTweet (str, code) {
      if (this.tweetContent.tweetWhy.length + this.tweetContent.tweetWhat.length + this.tweetContent.tweetHow.length < 20) {
        this.validation.validateResult = '20字以上入力してください'
      } else if (this.tweetContent.tweetWhy.length + this.tweetContent.tweetWhat.length + this.tweetContent.tweetHow.length > 87) {
        this.validation.validateResult = '熱入りすぎだよ！'
      } else {
        this.validation.validateResult = 'めっちゃいい理由！'
        var target = document.getElementById('TWEET')
        // var evp_box = document.getElementsByClassName('tweetBox')
        // console.log(evp_box)
        // var queryStr = location.search
        // var queryArr = queryStr.split('=')
        // var url = encodeURI(queryArr[1])
        // var text_all = ''
        // var text_all = this.evp_template.temp1 + evp_box[0].value + this.evp_template.temp2 + this.evp_template.temp3 + evp_box[1].value+ this.evp_template.temp4 + evp_box[2].value + this.evp_template.temp5 + url
        // TWEET.innerHTML = '<a class="button" href="https://twitter.com/intent/tweet?hashtags=Goodbuy&text=' + input_data + '" target="_blank">Tweet</a>'

        var textAll = this.evp_template.temp1 + this.tweetContent.tweetWhy + this.evp_template.temp2 + this.evp_template.temp3 + this.tweetContent.tweetWhat + this.evp_template.temp4 + this.tweetContent.tweetHow + this.evp_template.temp5
        var inputData = textAll.replace(/\r?\n/g, '%0D%0A')
        var path = 'https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text=' + inputData
        target.innerHTML = '<a href=' + path + '" target="_blank">Tweet</a>'
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
