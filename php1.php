<?php

$file = fopen("people.txt","a+");
echo fwrite($file,$_GET['name']."\n");
fclose($file);
?>
