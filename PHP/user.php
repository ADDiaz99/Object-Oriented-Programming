<?php
class User extends Account {
    public function __construct($name, $document, $email, $password){
        parent::($name, $document, $email, $password);
    }
}



?>