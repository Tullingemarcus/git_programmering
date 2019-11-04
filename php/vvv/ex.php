<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
.error {color: #FF0000;}
</style>
    </head>
    <body>

    <?php
// define variables and set to empty values
$CodeErr = "";
$Code = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST['UCode'])) {
    $CodeErr = "Code is required";
    #header("Location: vvv/ex.php");
  } 
  else {
    $Code = $_POST['UCode'];
    #header("Location: vvv/xe");
  }
}

#function test_input($data) {
 # $data = trim($data);
  #$data = stripslashes($data);
  #$data = htmlspecialchars($data);
  #return $data;
#}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field</span></p>
<form method="post" action=<?php $_SERVER['UCode']?>>  
  Code: <input type="text" name="UCode">
  <span class="error"> <?php echo $CodeErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
  <br><br>
</form>

<?php
if $CodeErr = $_POST['UCode'];{
    header("Location: vvv/ex.php")
    exit();
}




?>





    </body>
</html>