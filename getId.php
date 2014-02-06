<?php
$file = "2007list.txt";
$p=$_GET["lNo"];
$lines=file($file);echo $lines[$p];
fclose($file);



?>
