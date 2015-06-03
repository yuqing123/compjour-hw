google.load('visualization', '1', {packages: ['corechart', 'bar']});
google.setOnLoadCallback(drawGID);

    function drawGID() {
      var queryString = encodeURIComponent('SELECT A, B');

      var query = new google.visualization.Query(
          'https://docs.google.com/spreadsheets/d/1aG7a9UdqQ-1XNKimjMpMrHdi5iJ8u-bZzMadO-jVnAY/edit?usp=sharing' + queryString);
      query.send(handleQueryResponse);
    }

    function handleQueryResponse(response) {
      if (response.isError()) {
        alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
      }

      var options = {
        height: 400,
        width: 1000,
        title: 'Percentage of young adults (18 to 34) living with parents: 1960 to present',
        colors: ['#fd7e17'],
        hAxis: {
          format: ' ',
          gridlines: {
            count: 6
          }
        },
        vAxis: {

        }
      };

      var data = response.getDataTable();
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }

    