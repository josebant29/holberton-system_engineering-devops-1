# Update user file limit
exec { 'update':
  command => '/bin/sed -i "s/holberton.*//g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
