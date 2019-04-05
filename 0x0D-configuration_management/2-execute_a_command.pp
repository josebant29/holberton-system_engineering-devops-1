# Kills a process called killmenow

exec { 'pkill -f killmenow':
   path => '/usr/bin'
}
