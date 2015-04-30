import requests
import json
data_url = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

states = ['California', 'Florida', 'Maryland', 'New York']

thelist = []
thelist.append(["State", "Job Count"])
for s in states:
    atts = {'CountrySubdivision': s, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    value = "US-" + data[s]
    thelist.append([value, jobcount])



chartcode = """
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'};

        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));

        chart.draw(datatable, options);
      }
    </script>


      <div class="container">
        <h1 style="text-align:center">Hello chart</h1>
        <div id="mychart"></div>
      </div>
  </body>
</html>
"""


htmlfile = open("1-8.html", "w")
htmlfile.write(chartcode % thelist)
htmlfile.close()