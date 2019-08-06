# This Puppet manifest kills a process named killmenow

exec { 'pkill -f killmenow':
  creates => '/0x0A-configuration_management/killmenow',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/' ],
}