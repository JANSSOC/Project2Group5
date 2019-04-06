
function buildCharts(sample) {
  sample = 2016
  var url = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots

  d3.json(url).then(function(data){
    //var xValues = data.state
    //var yValues = data.classification
    var xValues = [2,5,6,9,10]
    var yValues = [90,40,50,80,40]
  var trace1 = {
    x: xValues,
    y: yValues
  /*text: textValues.map(String),
      mode: 'markers',
    marker: {
      size: markerSize,
      color: markerColor,
      opacity: markerColor,
      colorscale: "Earth" */
    }
  
  
  var data = [trace1];
  
  var layout = {
   x_axis: 'State'  
  };
  
  Plotly.newPlot('bar', data, layout);
  )};
};