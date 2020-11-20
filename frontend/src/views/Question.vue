<template>
  <v-app>
    <v-card>
      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
      <v-select
        outlined
        v-model="category"
        :items="items"
        item-text="label"
        item-value="value"
        label="買いたい商品のジャンルを選んでね"
        return-object
      ></v-select>
      <!-- </v-col>
      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      > -->
        <v-btn
          @click="getQuestion"
          dark
          rounded
          x-large
          >
          確定
        </v-btn>
      </v-col>
    </v-card>
  <viewQuestion :questionData="questionData[0]" />

</v-app>
</template>

<script>
// @ is an alias to /src
import viewQuestion from '@/components/viewQuestion.vue'
export default {
  name: 'Question',
  data () {
    return {
      items: [
        { label: '日用品・生活雑貨', value: '日用品・生活雑貨' },
        { label: '本', value: '本' },
        { label: 'ファッション・小物', value: 'ファッション・小物' },
        { label: 'スポーツ・アウトドア', value: 'スポーツ・アウトドア' },
        { label: 'コスメ', value: 'コスメ' },
        { label: 'その他', value: 'その他' }
      ],
      category: '',
      questionData: []
    }
  },
  components: {
    viewQuestion
  },
  methods: {
    async getQuestion () {
      this.questionData = []
      var postData = { category: this.category.value }
      const path = process.env.VUE_APP_BASE_URL + 'api/getquestion'
      // const self = this
      await this.$api
        .post(path, postData)
        .then(response => {
          this.questionData.push(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
