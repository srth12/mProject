<?php
$out=file_get_contents('php://input');
//$out=$_POST['output'];
$file = fopen("test.txt","a+");
fwrite($file,$out);
fclose($file);


?>
