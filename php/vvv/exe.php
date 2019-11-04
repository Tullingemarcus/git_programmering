
<?php
if(isset($_POST['submit'])){

 $code = $_POST['name'];

if(empty($code)){
  
  exit();
  }

else if (!preg_match("/^[A-F0-9]*$/", $code)) {
 
  exit();
  }
}
else{
  header("location: ../vvv/ex.php");
  exit();
}
?>