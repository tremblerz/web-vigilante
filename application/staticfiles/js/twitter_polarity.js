var chartData = generateChartData();

var chart = AmCharts.makeChart( "realtime_polarity", {
  "type": "serial",
  "theme": "light",
  "dataProvider": chartData,
  "valueAxes": [ {
    "position": "left",
    "title": "Tweet Polarity"
  } ],
  "graphs": [ {
    "valueField": "polarity"
  } ],
  "categoryField": "date",
  "categoryAxis": {
    "minPeriod": "mm",
    "parseDates": true
  }
} );

// generate some random data, quite different range
function generateChartData() {
  var chartData = [];
  // current date
  var firstDate = new Date();
  // now set 500 minutes back
  firstDate.setMinutes( firstDate.getDate() - 200 );

  // and generate 500 data items
  for ( var i = 0; i < 200; i++ ) {
    var newDate = new Date( firstDate );
    // each time we add one minute
    newDate.setMinutes( newDate.getMinutes() + i );
    // some random number
    var sign = Math.random();
    if (sign > 0.5)
      sign = -1;
    else
      sign = 1;

    var polarity = sign * Math.random();
    // add data item to the array
    chartData.push( {
      date: newDate,
      polarity: polarity
    } );
  }
  return chartData;
}

/**
 * An interval to add new data points
 */
