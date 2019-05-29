# Change Nginx open file limit
exec {
  command => '/bin/sed -ie \'s/-n 15/-n 2000/\' /etc/default/nginx'
}
exec {
  command => '/etc/init.d/nginx restart'
}
