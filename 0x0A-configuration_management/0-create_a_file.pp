# This Puppet manifest creates a file in /tmp called holberton

file { '/tmp/holberton':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}