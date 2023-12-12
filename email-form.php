<?php
    $name = $_POST['name'];
    $visitor_email = $_POST['email'];
    $message = $_POST['message'];

    $to = "W0491090@nscc.ca"
    $email_subject = "New Message from: $visitor_email"
    $headers = "From: $visitor_email \r\n";
    mail($to,$email_subject,$message,$headers)
?>