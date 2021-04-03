# makes changes to config file
include stdlib

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  match => 'PasswordAuthentication',
  line  => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton',
}
