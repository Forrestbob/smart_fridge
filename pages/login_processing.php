<?php
include("db_connect.php");
?>


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
	<head>
		<title>Form</title>
	</head>
	<body>

        <?php

            $email = $_POST["email"];
            $password = $_POST["password"];
        
            $email = stripcslashes($email); 
            $password = stripcslashes($password);
            $email = mysql_real_escape_string($email); 
            $password = mysql_real_escape_string($password);
        
            $result = mysql_query("SELECT * FROM customers WHERE email = '$email ' and password = '$password '") or die("failed to query " .mysql_error()); 
        
        $row = mysql_fetch_array($onnection, $result); 
        if($row['email'] == $email && $row['password'] == $password){
            echo "login sucess"; 
            
        }
               echo "login failed"; 
      
        ?>
            

	</body>
</html>
