# Change Nginx open file limit
exec { 'update':
  command => '/bin/sed -ie \'s/-n 15/-n 2000/\' /etc/default/nginx'
}
exec { 'restart':
  command => '/etc/init.d/nginx restart'
}
