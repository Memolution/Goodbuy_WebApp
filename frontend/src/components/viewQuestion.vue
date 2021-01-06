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
          <notBuy />
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
import notBuy from '@/components/notBuy.vue'
export default {
  data() {
    return {
      // status: 0,
      index: 0,
      tweetText: [],
      recentUrl: [],
      tweetUrl: [],
      visitCount: -1,
      levelUpMessage: []
    };
  },
  components: {
    notBuy
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
      if (typeof this.recentUrl[0] == 'undefined'){
        this.recentUrl[0] = ''
      }
      var target = document.getElementById("TWEET");
      const path = process.env.VUE_APP_BASE_URL + "api/question_to_tweet";
      const self = this;
      // let params = new URLSearchParams();
      var params = {
        question: {
          q0: this.questionData[0].content,
          q1: this.questionData[1].content,
          q2: this.questionData[2].content,
          q3: this.questionData[3].content,
        },
        url: this.recentUrl
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
    },
    show_message() {
      this.countAction()
      alert("お疲れ様でした！このタブを閉じて、お買い物を続けてください。");
    },
    print_action() {
      this.countAction()
      window.print();
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
  created() {
    this.recentUrl = [];
    var isUrl = this.$route.path;
    var wasUrl = isUrl.split("question/")[1];
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
