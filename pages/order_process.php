<?php
include("db_connect.php");
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

<?php
		
		// you don't use mysqli_free_result because it returns a boolran 
		
	?>
	
</html>

<?php  mysqli_close($connection) ?> 
