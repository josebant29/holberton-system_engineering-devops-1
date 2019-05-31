# Change Nginx open file limit
exec { 'update':
  command => 'sed -i "s/15/2000/" /etc/default/nginx && /etc/init.d/nginx restart',
  path  => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
}
