<template>
  <v-app>
    <v-card>
      <v-card-title>
        どれくらい買い物習慣が良くなったか確認しよう
      </v-card-title>
      <v-card-text>
      <h3>{{message[0].message}}</h3>
      </v-card-text>
      <section class="charts">
        <vue-highcharts
          :highcharts="Highcharts"
          :options="options"
          ref="chart"
        >
        </vue-highcharts>
      </section>
    </v-card>
  </v-app>
</template>

<script>
/* eslint-disable */
import VueHighcharts from "vue2-highcharts";
import More from "highcharts/highcharts-more";
import Highcharts from "highcharts";

More(Highcharts);
const data = {
  chart: {
    type: "gauge",
    plotBackgroundColor: null,
    plotBackgroundImage: null,
    plotBorderWidth: 0,
    plotShadow: false
  },

  title: {
    text: "購入理由を考えた回数"
  },

  pane: {
    startAngle: -150,
    endAngle: 150,
    background: [
      {
        backgroundColor: {
          linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
          stops: [[0, "#FFF"], [1, "#333"]]
        },
        borderWidth: 0,
        outerRadius: "109%"
      },
      {
        backgroundColor: {
          linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
          stops: [[0, "#333"], [1, "#FFF"]]
        },
        borderWidth: 1,
        outerRadius: "107%"
      },
      {
        // default background
      },
      {
        backgroundColor: "#DDD",
        borderWidth: 0,
        outerRadius: "105%",
        innerRadius: "103%"
      }
    ]
  },

  // the value axis
  yAxis: {
    min: 0,
    max: 100,

    minorTickInterval: "auto",
    minorTickWidth: 1,
    minorTickLength: 10,
    minorTickPosition: "inside",
    minorTickColor: "#666",

    tickPixelInterval: 30,
    tickWidth: 2,
    tickPosition: "inside",
    tickLength: 10,
    tickColor: "#666",
    labels: {
      step: 2,
      rotation: "auto"
    },
    title: {
      text: "考えた回数"
    },
    plotBands: [
      {
        from: 0,
        to: 10,
        color: "#61C28E"
      },
      {
        from: 10,
        to: 20,
        color: "#64C261"
      },
      {
        from: 20,
        to: 30,
        color: "#95C261" // green
      },
      {
        from: 30,
        to: 40,
        color: "#C2BF61" // green
      },
      {
        from: 40,
        to: 50,
        color: "#C28E61" // green
      },
      {
        from: 50,
        to: 60,
        color: "#C26164" // green
      },
      {
        from: 60,
        to: 70,
        color: "#C26195" // green
      },
      {
        from: 70,
        to: 80,
        color: "#BF61C2" // yellow
      },
      {
        from: 80,
        to: 90,
        color: "#8E61C2" // green
      },
      {
        from: 90,
        to: 100,
        color: "#6164C2" // red
      }
    ]
  },

  series: [
    {
      name: "Rank",
      data: [0],
      tooltip: {
        valueSuffix: "回数"
      }
    }
  ]
};
export default {
  components: {
    VueHighcharts
  },
  data() {
    return {
      visitCount: 0,
      options: data,
      Highcharts,
      message: []
    };
  },
  created () {
    if (localStorage.getItem('visitCount') == null) {
      localStorage.setItem('visitCount', 0)
      // this.visitCount = 0
    } else {
      this.visitCount = JSON.parse(localStorage.getItem('visitCount'))
    }
    this.options.series[0].data = [this.visitCount]
    // this.message = []

    const path = process.env.VUE_APP_BASE_URL + 'api/viewLevel'
    // const self = this
    const self = this;
    var params = {
      visitCount: {
        count: this.visitCount
      },
    };
    this.$api
      .post(path, params)
      .then(response => {
        this.message.push(response.data)
      })
      .catch(error => {
        console.log(error)
      })
  }
};

</script>
