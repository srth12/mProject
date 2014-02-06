<?php
session_start();
mkdir("data2007");
$out=file_get_contents('php://input');
//$out=file_get_contents('output');
//$out=$_POST['output'];
$file = fopen("./data2007/test".$_SESSION['count'].".txt","w");
//$file = fopen("./data/test.txt","a+");
fwrite($file,$out);
fclose($file);
$_SESSION['count']+=1;

?>
