<?php
require_once('car.php');
require_once('uberX.php');
require_once('uberPool.php');
require_once('account.php');

$car = new Car("AW456", new Account("Andres Herrera", "AMS123"));
$car->printDataCar();

$uberX = new UberX("DSA548", new Account("Andres Herrera","1001545496", "Chevrolet","Spark"));
$uberX->printDataCar();

$uberPool = new UberPool("FDS875", new Account("Pedro Perez","1015421489", "Chevrolet","Camaro"));
$uberPool->printDataCar();








?>