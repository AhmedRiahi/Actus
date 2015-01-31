var server_host = 'http://localhost:8001/';
var refresh_tempo = 10000;


google.load("visualization", "1", {packages:["corechart"]});

google.setOnLoadCallback(loadRankingData);

function loadRankingData(){
	$.ajax({
		type: "GET",
		url: server_host,
		success: function(response){
			console.log(response);
			drawChart(response);
			
		},
		error: function(response){
		  console.log('error');
		  console.log(response);
		}
    });
} 

function drawChart(data){
	var dataView = [['Web site','Occurence', { role: 'annotation' }]];

	for(var i=0;i<data.length;i++){
		dataView.push([data[i][0],data[i][2],data[i][1]]);
	}
	console.log(dataView);
	var data = google.visualization.arrayToDataTable(dataView);
	var chart = new google.visualization.BarChart(document.getElementById('chart'));
	chart.draw(data);
}

setInterval(loadRankingData,refresh_tempo);