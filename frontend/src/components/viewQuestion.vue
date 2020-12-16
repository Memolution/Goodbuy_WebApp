<template>
  <div>
    <v-app>
      <p v-if="this.status == 0">
        <v-card light elevation="16">
          <v-divider class="mx-3"></v-divider>
          <v-card-text class="text-center">
            <div class="body-1 mb-1">
              <h2>{{ questionData[index].content }}</h2>
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
          <v-card-text class="text-center">
            <div class="body-1 mb-1">
              <v-alert outlined type="warning" prominent border="left">
                <h2>買いたい商品を思い浮かべながらもう少し考えてみよう</h2>
              </v-alert>
            </div>
          </v-card-text>
          <p v-for="data in questionData" :key="data.id">
            <v-card light elevation="16">
              <v-divider class="mx-3"></v-divider>
              <v-card-text class="text-center">
                <div class="body-1 mb-1">
                  <h2>{{ data.content }}</h2>
                </div>
              </v-card-text>
            </v-card>
          </p>
        </v-card>
      </p>

      <p v-else-if="this.status == -1">
        <v-card light elevation="16">
          <v-divider class="mx-3"></v-divider>
          <v-card-text class="text-center">
            <div class="body-1 mb-1">
              <v-alert outlined type="success" prominent border="left">
                <h2>買おう！</h2>
                <br />
                <h3>あなたは以下の質問に答えました.</h3>
                <p v-for="data in questionData" :key="data.id">
                  <v-card light elevation="16">
                    <v-divider class="mx-3"></v-divider>
                    <v-card-text class="text-center">
                      <div class="body-1 mb-1">
                        <h2>{{ data.content }}</h2>
                      </div>
                    </v-card-text>
                  </v-card>
                </p>
                <v-card-actions>
                  <v-btn text v-on:click="conversionQuestion" id="TWEET">
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
  data() {
    return {
      // status: 0,
      index: 0,
      tweetText: [],
      recentUrl: []
    };
  },
  props: {
    questionData: {
      type: Array,
    },
    status: {},
  },
  methods: {
    breakPoint() {
      // alert('もう少し考えてからまた来てね')
      this.index = 0;
      this.status = 1;
      // this.$emit('catchStatus', 1)
    },
    nextQuersiton() {
      if (this.index < this.questionData.length - 1) {
        // console.log(this.index)
        this.index += 1;
      } else {
        // alert('買おう！')
        this.index = 0;
        this.status = -1;
        // this.$emit('catchStatus', -1)
      }
    },
    conversionQuestion() {
      this.tweetText = [];
      var target = document.getElementById("TWEET");
      const path = process.env.VUE_APP_BASE_URL + "api/question_to_tweet";
      const self = this;
      // let params = new URLSearchParams();
      var params = {
        question: {
          q0: this.questionData[0].content,
          q1: this.questionData[1].content,
          q2: this.questionData[2].content,
        },
      };
      console.log(params);
      this.$api
        .post(path, params)
        .then((response) => {
          this.tweetText.push(response.data);
          // var inputData += this.recentUrl[0];
          var inputData = (this.tweetText[0].text + this.recentUrl[0]).replace(
            /\r?\n/g,
            "%0D%0A"
          );
          var path =
            "https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text=" +
            inputData;
          target.innerHTML = "<a href=" + path + ">Tweet</a>";
        })
        .catch((error) => {
          console.log(error);
        });
    },
    GetTweet(str, code) {
      var textAll = "";
      var target = document.getElementById("TWEET");
      for (let i = 0; i < this.questionData.length; i++) {
        console.log(this.questionData[i].content);
        textAll += this.questionData[i].content;
      }
      // this.recentUrl;
      var inputData = textAll.replace(/\r?\n/g, "%0D%0A");
      var path =
        "https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text=" +
        inputData;
      target.innerHTML = "<a href=" + path + ">Tweet</a>";
    },
    show_message() {
      // this.message = "お疲れ様でした!"
      alert("お疲れ様でした！このタブを閉じて、お買い物を続けてください。");
    },
    print_action() {
      window.print();
    }
  },
  created() {
    this.recentUrl = [];
    var isUrl = this.$route.path;
    var wasUrl = isUrl.split("question/")[1];
    this.recentUrl.push(wasUrl);
  }
};
</script>
