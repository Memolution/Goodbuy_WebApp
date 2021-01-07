<template>
  <div>
    <v-app>
      <v-card>
        <v-card-title>買わない理由を自由記述で書いてみよう</v-card-title>
        <details>
          <summary>記入例</summary>
          原付と黄色のヘルメットを買いたいと思いました。<br />
          しかし、免許を持っていませんでした。<br />
          二人乗りもできないという事実を踏まえて、買わないことにしました。<br />
        </details>
        <!-- <br /> -->
        <v-textarea
          outlined
          rows="10"
          name="input-7-4"
          v-model="tweetContent.tweetWhy"
          label="買わない理由を入力してね"
        >
          >
        </v-textarea>
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
          {{ validation.validateResult }}
        </v-alert>
      </div>
      <div
        v-else-if="
          this.validation.validateResult == '20字以上入力してください' ||
          this.validation.validateResult == '熱入りすぎだよ！'
        "
      >
        <v-alert outlined type="warning" prominent border="left">
          {{ validation.validateResult }}
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
      tweetContent: {
        tweetWhy: '',
      },
      validation: {
        validateResult: '',
      },
      recentUrl: [],
      message: '',
      tweetUrl: []
    };
  },
  methods: {
    postTweet () {
      this.tweetUrl = [];
      if ( this.tweetContent.tweetWhy.length < 20) {
        this.validation.validateResult = '20字以上入力してください';
      } else if ( this.tweetContent.tweetWhy.length > 87) {
        this.validation.validateResult = '熱入りすぎだよ！';
      } else {
        var target = document.getElementById("TWEET");
        this.validation.validateResult = 'めっちゃいい理由！';
        const path = process.env.VUE_APP_BASE_URL + "api/content_to_tweet";
        const self = this;
        // let params = new URLSearchParams();
        // this.tweetText.tweetWhy = this.tweetText.tweetWhy.replace(/\r?\n/g, '\\n');
        console.log(this.tweetContent.tweetWhy)
        var textAll = this.tweetContent.tweetWhy + this.recentUrl
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
    print_action() {
      window.print();
    },
    show_message() {
      // this.message = 'お疲れ様！';
      alert('お疲れ様でした！いい判断だと思いますよ。このタブを閉じて、お買い物を続けてください。')
    },
  },
  created() {
    this.recentUrl = [];
    var isUrl = this.$route.path;
    var wasUrl = isUrl.split('will/')[1];
    this.recentUrl.push(wasUrl);
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

details {
  border: 1px solid #aaa;
  border-radius: 4px;
  padding: 0.5em 0.5em 0;
}

summary {
  font-weight: bold;
  margin: -0.5em -0.5em 0;
  padding: 0.5em;
}

details[open] {
  padding: 0.5em;
}

details[open] summary {
  border-bottom: 1px solid #aaa;
  margin-bottom: 0.5em;
}
</style>
