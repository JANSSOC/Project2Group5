
//function buildCharts(sample) {
console.log("i do not like green eggs n ham");
var url = `/years`;
 // var url = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
d3.json(url).then(function(data){

  console.log(data);
    
    var xValues = data.year_reported
    var yValues = data.state
    
    var trace1 = {
      x: Object.values(xValues),
      y: Object.values(yValues),
      type: 'bar'
    }
  
  var data = [trace1];
  
  var layout = {
   x_axis: 'State'  
  }
  
  Plotly.newPlot("bar", data, layout);
});  


var url2 = `/recallingFirm`;
console.log("what the world needs now is love sweet love")
 // var url = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
d3.json(url2).then(function(data2){

  console.log(data2);
    
    var xValues = data2.year_reported
    var yValues = data2.recalling_firm
    
    var trace1 = {
      x: Object.values(xValues),
      y: Object.values(yValues),
      type: 'bar'
    }
  
  var data = [trace1];
  
  var layout = {
   x_axis: 'Recalling Firm'  
  }
  
  Plotly.newPlot("firmBar", data, layout);
});  

var url3 = `/classification`;
console.log("what the world needs now is love sweet love")
 // var url = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
d3.json(url3).then(function(data3){

  console.log(data3);
    
  var xValues = data3.year_reported
  var yValues = data3.classification


  var data = [{
  
    values: Object.values(xValues),
    labels:Object.values(yValues),
    type: 'pie'
  }];

  var layout = {
    height: 800,
    width: 500
  };

Plotly.newPlot('pie', data, layout);
});
//buildCharts();
/*
function init() {
  console.log("hello");

  var selector = d3.select("#selDataset");
  // Grab a reference to the dropdown select element
  d3.json("/years").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample); 
  });
}
init();*/
