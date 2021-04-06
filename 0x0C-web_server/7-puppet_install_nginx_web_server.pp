# installs and configures nginx
include stdlib

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file_line { 'Holberton School':
  path => '/var/www/html/index.html',
  line => 'Holberton School',
}

file_line {'Redirect Me':
  path  => '/etc/nginx/sites-available/default',
  after => Pattern[/^\s+server_name .+;/],
  line  => "\tlocation /redirect_me {\n\t\treturn 301 https://bit.ly/3rTuCnC;\n\t}",
}
