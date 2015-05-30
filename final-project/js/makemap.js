
var width = 960,
    height = 500;

var color = d3.scale.threshold()
    .domain([-40, -20, 0, 20, 40])
    .range(["#f2f0f7", "#dadaeb", "#bcbddc", "#9e9ac8", "#756bb1", "#54278f"]);

var path = d3.geo.path();

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

queue()
    .defer(d3.json, "./data/us.json")
    .defer(d3.csv, "./data/percentage_change.csv")
    .await(ready);


  var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    console.log('hey')
    return "<strong>Frequency:</strong> <span style='color:red'>" +  'hello' + "</span>";
  })
  svg.call(tip);



function ready(error, us, unemployment) {
  var rateById = {};



  unemployment.forEach(function(d) { 
    rateById[d.fips] = +d.percentage_change; 
  });

  svg.append("g")
      .attr("class", "counties")
    .selectAll("path")
      .data(topojson.feature(us, us.objects.counties).features)
    .enter().append("path")
      .attr("d", path)
      .style("fill", function(d) { return color(rateById[d.id]); });

  svg.append("path")
      .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a.id !== b.id; }))
      .attr("class", "states")
      .attr("d", path)
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)
}

