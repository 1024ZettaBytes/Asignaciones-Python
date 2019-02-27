<?php
$dbServerName = "10.10.1.101\SQLMEGA";
$dbUsername = "Kborboa";
$dbPassword = "Omega123";
$dbName = "CARTERA";

// create connection
$conn = new mysqli($dbServerName, $dbUsername, $dbPassword, $dbName);

// check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>