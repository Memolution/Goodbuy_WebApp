<template>
  <div>
    <v-app>
      <v-card>
        <v-card-title
          >購入理由をエレベーターピッチ風に書いてみよう</v-card-title
        >
        <v-card-text>
          <br />
          <h3>{{ evp_template.temp1 }}</h3>

          <v-text-field
            v-model="tweetContent.tweetWhy"
            label="購買動機を入力してね"
          >
          </v-text-field>

          <h3>{{ evp_template.temp2 }}</h3>
          <br />
          <h3>{{ evp_template.temp3 }}</h3>

          <v-text-field
            v-model="tweetContent.tweetWhat"
            label="どんな問題が解決できるか入力してね"
          >
          </v-text-field>

          <br />
          <h3>{{ evp_template.temp4 }}</h3>
          <v-text-field
            v-model="tweetContent.tweetHow"
            label="どのようにして解決できそうか入力してね"
          >
          </v-text-field>

          <br />
          <h3>{{ evp_template.temp5 }}</h3>
        </v-card-text>
        <v-text-field v-model="recentUrl" label="商品のURLを入力してね">
        </v-text-field>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn text v-on:click="postTweet" id="TWEET">
            <v-icon>mdi-twitter</v-icon>
            ツイートする
          </v-btn>
          <v-btn text v-on:click="print_action">
          <v-icon>mdi-download</v-icon>
            保存する
          </v-btn>
          <v-btn text v-on:click="show_message">
            <v-icon>mdi-account-check-outline</v-icon>
            完了
          </v-btn>
        </v-card-actions>
      </v-card>
      <div v-if="this.validation.validateResult == 'めっちゃいい理由！'">
        <v-alert outlined type="success" prominent border="left">
          <h2>{{ validation.validateResult }}</h2>
        </v-alert>
      </div>
      <div
        v-else-if="this.validation.validateResult == '20字以上入力してください' || this.validation.validateResult== '熱入りすぎだよ！'">
        <v-alert outlined type="warning" prominent border="left">
          <h2>{{ validation.validateResult }}</h2>
        </v-alert>
      </div>
    </v-app>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'willForm',
  data: function () {
    return {
      evp_template: {
        temp1: 'この商品は、',
        temp2: 'を解決する事を目的に買います。',
        temp3: 'これがあると',
        temp4: 'を',
        temp5: '(して)問題を解決できます。',
        temp6: 'これは、今の私の所持品では代替',
        temp7: '。',
      },
      tweetContent: {
        tweetWhy: '',
        tweetWhat: '',
        tweetHow: '',
      },
      validation: {
        validateResult: '',
      },
      recentUrl: [],
      message: '',
      tweetUrl: [],
      visitCount: -1,
      levelUpMessage: []
    };
  },
  methods: {
    print_action() {
      this.countAction()
      window.print();
    },
    show_message () {
      this.countAction()
      alert('お疲れ様でした！このタブを閉じて、お買い物を続けてください。')
    },
    postTweet () {
      this.tweetUrl = [];
      if ( this.tweetContent.tweetWhy.length + this.tweetContent.tweetWhat.length + this.tweetContent.tweetHow.length < 20) {
        this.validation.validateResult = '20字以上入力してください';
      } else if ( this.tweetContent.tweetWhy.length + this.tweetContent.tweetWhat.length + this.tweetContent.tweetHow.length > 87) {
        this.validation.validateResult = '熱入りすぎだよ！';
      } else {
        // this.countAction()
        var target = document.getElementById("ツイートする");
        this.validation.validateResult = 'めっちゃいい理由！';
        const path = process.env.VUE_APP_BASE_URL + "api/content_to_tweet";
        const self = this;
        // let params = new URLSearchParams();
        var textAll = this.evp_template.temp1 + this.tweetContent.tweetWhy + this.evp_template.temp2 + this.evp_template.temp3 + this.tweetContent.tweetWhat + this.evp_template.temp4 + this.tweetContent.tweetHow + this.evp_template.temp5 + this.recentUrl;
        var params = {
          tweet: {
            content: textAll
          },
        };
        console.log(params);
        this.$api
          .post(path, params)
          .then((response) => {
            this.tweetUrl.push(response.data);
            target.innerHTML = this.tweetUrl[0]['url'];
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    countAction () {
      this.levelUpMessage = []
      this.visitCount += 1
      localStorage.setItem('visitCount', this.visitCount)
      if (this.visitCount % 5 == 0){
        // API叩く
        const path = process.env.VUE_APP_BASE_URL + "api/visitCount";
        const self = this;
        var params = {
          visitCount: {
            count: this.visitCount
          },
        };
        console.log(params);
        this.$api
          .post(path, params)
          .then((response) => {
            this.levelUpMessage.push(response.data);
            alert(this.levelUpMessage[0].message)
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
  },
  created () {
    this.recentUrl = [];
    var isUrl = this.$route.path;
    var wasUrl = isUrl.split('will/')[1];
    this.recentUrl.push(wasUrl);
  },
  mounted () {
    if (localStorage.getItem('visitCount') == null) {
      localStorage.setItem('visitCount', 1)
    } else {
      this.visitCount = JSON.parse(localStorage.getItem('visitCount'))
    }
  }
};
</script>

<style lang="scss">
.tweetBox {
  border: 2px solid #00aced;
  border-radius: 0.67em;
  padding: 0.5em;
  background-color: snow;
  width: 50em;
  height: 15px;
  font-size: 1em;
  line-height: 1.2;
}
#TWEET {
  width: 150px;
  height: 30px;
  line-height: 30px;
  text-align: center;

  background-color: #55acee;
  border: 2px solid #55acee;
  border-radius: 20px;
  color: #fff;
  padding: 4px 32px;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
#TWEET:hover {
  background-color: #fff;
  color: #55acee;
}
.error {
  color: red;
}
</style>
