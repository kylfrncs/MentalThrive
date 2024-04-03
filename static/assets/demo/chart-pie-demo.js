// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["COA", "CCJE", "CITE", "CAHS", "COED", "COME", "COM", "CME"],
    datasets: [{
      data: [12.21 , 15.58 , 11.25 , 8.32 , 13.14 , 13.26 , 14.13 , 12.11 ],
      backgroundColor: ['#DFFF00', '#FF7F50', '#FFBF00','#DE3163', '#9FE2BF'  ,'#40E0D0', '#6495ED', '#CCCCFF'],
    }],
  },
});
