<?php

$output=$_GET['output'];
$file = fopen("test.txt","w");
fwrite($file,$output);
fclose($file);


?>
