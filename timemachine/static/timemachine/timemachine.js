function loadData(dataType) {
	document.getElementById('main').innerHTML="http://google.com";
	var iframe = document.getElementById('statsview');
	iframe.src = dataType;
}