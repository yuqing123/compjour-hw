var width = 960,
 height = 500;
 var color_domain = [ -30, -20, -10, 0, 10, 20, 30, 40]
 var ext_color_domain = [ -40, -30, -20, -10, 0, 10, 20, 30, 40]
 var legend_labels = ["< -30%", "< -20%", "< -10%", "-10% to 0", "0 to 10%", "> 10%", "> 20%", "> 30%", "> 40%"]
 var color = d3.scale.threshold()
 .domain(color_domain)
 .range(["#303c56", "#236386", "#6FAFD3", "#BDD9E8", "#fee4ab", "#ffd862", "#fdaf17", "#fd7e17", "#fd4817"]);
 
var div = d3.select("body").append("div")
 .attr("class", "tooltip")
 .style("opacity", 0);
 
var svg = d3.select("body").append("svg")
 .attr("width", width)
 .attr("height", height)
 .style("margin", "10px auto");
 var path = d3.geo.path()
 
queue()
 .defer(d3.json, "./data/us.json")
 .defer(d3.csv, "./data/percentage_change.csv")
 .await(ready);
 
function ready(error, us, data) {
 var pairRateWithId = {};
 var pairNameWithId = {};
 
data.forEach(function(d) {
 pairRateWithId[d.fips] = +d.percentage_change;
 pairNameWithId[d.fips] = d.name_x;
 });
 svg.append("g")
 .attr("class", "county")
 .selectAll("path")
 .data(topojson.feature(us, us.objects.counties).features)
 .enter().append("path")
 .attr("d", path)
 .style ( "fill" , function (d) {
 return color (pairRateWithId[d.id]);
 })
 .style("opacity", 0.8)
 .on("mouseover", function(d) {
 d3.select(this).transition().duration(300).style("opacity", 1);
 div.transition().duration(300)
 .style("opacity", 1)
 div.text(pairNameWithId[d.id] + " : " + pairRateWithId[d.id])
 .style("left", (d3.event.pageX) + "px")
 .style("top", (d3.event.pageY -30) + "px");
 })
 .on("mouseout", function() {
 d3.select(this)
 .transition().duration(300)
 .style("opacity", 0.8);
 div.transition().duration(300)
 .style("opacity", 0);
 })
 
 };
 
var legend = svg.selectAll("g.legend")
 .data(ext_color_domain)
 .enter().append("g")
 .attr("class", "legend");
 
var ls_w = 20, ls_h = 20;
 
legend.append("rect")
 .attr("x", 20)
 .attr("y", function(d, i){ return height - (i*ls_h) - 2*ls_h;})
 .attr("width", ls_w)
 .attr("height", ls_h)
 .style("fill", function(d, i) { return color(d); })
 .style("opacity", 0.8);
 
legend.append("text")
 .attr("x", 50)
 .attr("y", function(d, i){ return height - (i*ls_h) - ls_h - 4;})
 .text(function(d, i){ return legend_labels[i]; });