# creating custom HTTP header
include stdlib

exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get-update'],
}

file_line { 'X-Served-By':
  path    => '/etc/nginx/sites-available/default',
  after   => '^\s+server_name .+;',
  line    => "\n\tadd_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  restart => 'service nginx restart',
  require => Package['nginx'],
}
