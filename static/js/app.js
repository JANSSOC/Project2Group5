function buildCharts(sample) {
  var url = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(url).then(function(data){
    var xValues = data.state;
    var yValues = data.state.;

  var trace1 = {
    x: xValues,
    y: yValues,
    text: textValues.map(String),
    mode: 'markers',
    marker: {
      size: markerSize,
      color: markerColor,
      opacity: markerColor,
      colorscale: "Earth"
    }
  };
  
  var data = [trace1];
  
  var layout = {
   x_axis: 'State'
    
  };
  
  Plotly.newPlot('bar', data, layout);