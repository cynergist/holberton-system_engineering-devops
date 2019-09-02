# This Puppet manifest kills a process named killmenow

exec { 'pkill -f':
  command => 'pkill -f killmenow',
  path    => [ '/usr/bin/' ],
}
