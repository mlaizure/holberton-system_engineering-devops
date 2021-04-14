# installs and configures nginx
include stdlib

exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get-update'],
}

file_line { 'Holberton School':
  path    => '/var/www/html/index.html',
  line    => "Holberton School",
  require => Package['nginx'],
}

file_line { 'Redirect Me':
  path    => '/etc/nginx/sites-available/default',
  after   => '^\s+server_name .+;',
  line    => "\tlocation /redirect_me {\n\t\treturn 301 https://bit.ly/3rTuCnC;\n\t}",
  require => Package['nginx'],
}

file { 'Error Page Text':
  ensure  => 'file',
  path    => '/var/www/html/my_404.html',
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

file_line { 'Error Page Config':
  path    => '/etc/nginx/sites-available/default',
  after   => '^\s+server_name .+;',
  line    => "\terror_page 404 /my_404.html;\n\tlocation /my_404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}",
  require => File['Error Page Text'],
}

service { 'nginx':
  ensure  => 'running',
  restart => 'service nginx restart',
  require => Package['nginx'],
}
