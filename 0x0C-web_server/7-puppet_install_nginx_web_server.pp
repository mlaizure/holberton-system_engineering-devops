# installs and configures nginx
include stdlib

exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

-> package { 'nginx':
  ensure => 'installed',
}

-> file_line { 'Holberton School':
  path => '/var/www/html/index.html',
  line => 'Holberton School',
}

-> file_line { 'Redirect Me':
  path  => '/etc/nginx/sites-available/default',
  after => '^\s+server_name .+;',
  line  => "\tlocation /redirect_me {\n\t\treturn 301 https://bit.ly/3rTuCnC;\n\t}",
}

-> file { 'Error Page Text':
  path    => '/var/www/html/my_404.html',
  content => "Ceci n'est pas une page",
}

-> file_line { 'Error Page Config':
  path  => '/etc/nginx/sites-available/default',
  after => '^\s+server_name .+;',
  line  => "\terror_page 404 /my_404.html;\n\tlocation /my_404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}",
}

-> service { 'nginx':
  ensure  => 'running',
  restart => 'service nginx restart',
}
