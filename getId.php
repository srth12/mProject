<?php
$file = "2005list.txt";
$p=$_GET["lNo"];
$lines=file($file);echo $lines[$p];
fclose($file);



?>
