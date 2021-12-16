// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['大专', '本科', '中专', '硕士', '高中', '中技',  '博士', '初中及以下'],
    datasets: [{
      label: "學歷",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [2084, 1918, 67, 44, 26, 17, 1, 1],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        // time: {
        //   unit: 'month'
        // },
        gridLines: {
          display: false
        },
        ticks: {
          // maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 2090,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
