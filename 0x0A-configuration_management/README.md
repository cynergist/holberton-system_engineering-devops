# 0x0A Configuration management

## Resources
[Digital Ocean's Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management) </br >
[Puppet Emacs mode](https://github.com/voxpupuli/puppet-mode/blob/master/README.md) </br >
[Puppet-lint](http://puppet-lint.com/) </br >
[Puppet's Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppet%E2%80%99s-declarative-language-modeling-instead-of-scripting) </br >
[The Puppet Language Style Guide](https://puppet.com/docs/puppet/6.7/style_guide.html) </br >
[Getting Started with Puppet Code: Manifests & Modules](https://www.digitalocean.com/community/tutorials/getting-started-with-puppet-code-manifests-and-modules) </br >
[Puppet Resource Type: file](https://puppet.com/docs/puppet/3.8/types/file.html) </br >

## Tasks

0. Create a file // 0-create_a_file.pp

Using Puppet, create a file in /tmp.

Requirements:

- File path is /tmp/holberton
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains I love Puppet

1. Install a package // 1-install_a_package.pp

Using Puppet, install puppet-lint.

Requirements:

- Install puppet-lint
- Version must be 2.1.1

2. Execute a command // 2-execute_a_command.pp

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

- Must use the exec Puppet resource
- Must use pkill
