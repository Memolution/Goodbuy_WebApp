<template>
  <v-app>
    <div>
      <v-card>
        <v-card-title>プロダクトの紹介</v-card-title>
        <!-- <p class="text-justify"> -->
        <v-card-text class="font-weight-medium">
          [Goodbuy] は[目的のない買い物]を解決したい[慎重に買い物をしたい人]向けの[Webサービス]です。<br />
          これは [購入理由を記述するタイミングを与えること] によって、[家計簿・買い物リスト] とは違って[理にかなった買い物] を実現できます。
        </v-card-text>
      </v-card>
      <br />
    </div>
    <v-divider inset></v-divider>
    <v-card>
      <v-card-title>使い方</v-card-title>
      <v-card-text class="font-weight-medium">
        Formでは、商品に対する購入理由を書くことができます。MenuのFormから記述ページに移動した後、
        ページ上部にあるタブから記述方法を選択できます。<br />
        「エレベーターピッチ風」を選択した場合、穴埋め形式で購入理由を記述できます。<br />
        「自由記述」を選択した場合、自由に理由を記述してもらえます。  <br />
        Chromeの拡張機能を用いて本アプリを起動した場合、自動的に商品ページのURLは記入されます。もちろん自分で打ち込んでいただいても構いません。<br />
        書いた理由は「ツイートする」ボタンをダブルクリックすることで、商品ページURLと一緒にTwitterで共有することもできます。<br />
      </v-card-text>
    </v-card>
    <v-divider inset></v-divider>
    <br />
    <v-card>
      <v-card-title>拡張機能</v-card-title>
      <v-card-text class="font-weight-medium">
        <a href="https://github.com/Memolution/buybye/releases">最新版リリースノート</a>のSourceCode(zip)をダウンロードしてください。
        <br />追加方法は
        <a
          href="https://github.com/Memolution/buybye#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%99%82%E3%81%AB%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8"
        >こちら</a>
      </v-card-text>
    </v-card>
  </v-app>
</template>

<script>
/* eslint-disable */
export default {
  name: "HelloWorld",
  data: () => ({})
};
</script>
