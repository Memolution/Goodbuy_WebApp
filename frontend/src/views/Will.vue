<template>
    <v-app>
      <v-card>
        <v-col
          class="d-flex"
          cols="12"
          sm="6"
        >
        <v-select
          label="フォームの種類を選んでね"
          :items="formItems"
          v-model="formType"
          required>
        </v-select>
      <!-- <v-btn
        @click="getFormType"
        dark
        rounded
        x-large>
        確定
      </v-btn> -->
    </v-col>
    </v-card>
    <p v-if="this.formType == 'エレベーターピッチ風' ">
      <WillForm />
    </p>
    <p v-else-if="this.formType == '自由記述' ">
      <freeWillForm />
    </p>
  </v-app>
</template>

<script>
// @ is an alias to /src
import WillForm from '@/components/WillForm.vue'
import freeWillForm from '@/components/FreeWillForm.vue'
export default {
  name: 'Will',
  data () {
    return {
      formItems: ['エレベーターピッチ風', '自由記述'],
      formType: 'エレベーターピッチ風'
    }
  },
  components: {
    WillForm,
    freeWillForm
  }
}
</script>
