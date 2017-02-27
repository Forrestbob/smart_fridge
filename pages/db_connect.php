<?php
  // 1. Create a database connection
  $dbhost = "localhost";
  $dbuser = "DataBAEs";
  $dbpass = "DataBAEs";
  $dbname = "smart_fridge";
  $connection = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
  // Test if connection succeeded
  if(mysqli_connect_errno()) {
    die("Database connection failed: " . 
         mysqli_connect_error() . 
         " (" . mysqli_connect_errno() . ")"
    );
  }
?>