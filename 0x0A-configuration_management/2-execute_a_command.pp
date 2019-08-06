# This Puppet manifest kills a process named killmenow

exec { 'pkill -f killmenow':
  cwd     => '/vagrant/Documents/holberton-system_engineering-devops/0x0A-configuration_management/',
  creates => '/0x0A-configuration_management/killmenow',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/' ],
}