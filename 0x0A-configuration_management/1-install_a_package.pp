# This Puppet manifest installs a package for puppet-lint

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}