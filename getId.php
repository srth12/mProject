<?php
$file = "2008list.txt";
$p=$_GET["lNo"];
$lines=file($file);echo $lines[$p];
fclose($file);



?>
