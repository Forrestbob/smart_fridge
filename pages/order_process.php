<?php
  // 1. Create a database connection
  $dbhost = "localhost";
  $dbuser = "root";
  $dbpass = "";
  $dbname = "test_db";
  $connection = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
  // Test if connection succeeded
  if(mysqli_connect_errno()) {
    die("Database connection failed: " . 
         mysqli_connect_error() . 
         " (" . mysqli_connect_errno() . ")"
    );
  }
?>
    
    <?php
    if(isset($_POST["submit"])){   
    
    
    
    $query2 = "INSERT INTO orders (customerID, productID, quantity)
                VALUES(1001, 1001, 1)"; 
    
       
 $updateResult = mysqli_query($connection, $query2);
        
         if ($updateResult) {
		echo "Success!"; 
	} else {
        
        die("Database query failed. " . mysqli_error($connection));
    }        
        
    }

	// Test if there was a query error


	?>

<html>

    
                           
                        
                         <button type="submit" name="submit" class="btn btn-outline btn-primary btn-lg"><a href="http://localhost/smartfridge_final/pages/dashboard">Return to Dashboard</a></button>
                
        
</html>

<?php  mysqli_close($connection) ?> 
