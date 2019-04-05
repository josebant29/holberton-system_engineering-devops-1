# Kills a process called killmenow

exec { 'pkill killmenow':
   command => pkill -f killmenow
}
