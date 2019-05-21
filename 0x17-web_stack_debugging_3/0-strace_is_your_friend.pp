# Fix typo
exec { 'fix':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php'
}

exec { 'restart':
  command => '/etc/init.d/apache2 restart'
}
