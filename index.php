<html>
<head>
<script type="text/javascript">

// IMDb ID to Search
var imdbId = 1285016;

// Send Request

var http = new XMLHttpRequest();
var omdbData="";
<?php


session_start();
$_SESSION["count"]=107;
?>
for(var i=107;i<1900;i++){
var output='';
var l="";


http.open("GET","getId.php?lNo="+i,false);

http.send();

l=http.responseText;

http.open("GET", "http://www.omdbapi.com/?tomatoes=True&i=" + l, false);
http.send();

// Response to JSON

output=http.responseText;//





http.open("POST","write.php",false);
http.setRequestHeader('Content-Type', 'text/plain');
http.setRequestHeader("Content-length", output.length);
http.setRequestHeader("Connection", "close");
http.send(output);


document.write(output);
}

</script>
</head>
</html>
