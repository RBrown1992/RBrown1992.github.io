<?php
    #this .php file would be used to send emails to my school email address from the imputted information given in the form on the Contact page of my website
    #as GitHub io does not support .php file execution, this functionality of the website is not operational
    #a web server with .php allowed would be required to propely implement this
    #for the sake of this assigment, this .php file and html reference to it was included for demonstration purposes

    #adapted from: https://html.form.guide/email-form/php-form-to-email/

    #get variables from form set to this .php file (<form class="emailForm" action="email-form.php" method="POST" name="EmailForm"> line from contact.html)
    #variables of name, sender email address, and message
    $name = $_POST['name'];
    $visitor_email = $_POST['email'];
    $message = $_POST['message'];

    #set variable of the receipient email addree to my school email
    $to = "W0491090@nscc.ca"
    #construct variable to store the email subject, based on sender email address
    $email_subject = "New Message from: $visitor_email"
    #construct variable to stor header information, based on sender email address
    $headers = "From: $visitor_email \r\n";
    #sends email, based on above defined variables
    mail($to,$email_subject,$message,$headers)
?>