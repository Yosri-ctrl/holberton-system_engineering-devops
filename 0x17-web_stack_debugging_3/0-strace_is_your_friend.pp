# fixing the error of "no such a file or directory
exec { 'fixing typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin']
}