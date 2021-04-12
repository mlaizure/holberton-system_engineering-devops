# creating custom HTTP header
include stdlib

file_line { 'Redirect Me':
  path  => '/etc/nginx/sites-available/default',
  after => '^\s+server_name .+;',
  line  => "\n\tadd_header X-Served-By ${hostname};",
}
