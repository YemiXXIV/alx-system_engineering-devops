# install and configure Nginx
package { 'nginx':
  ensure => 'installed',
}

exec { 'set_hello_world':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.ngin\
x-debian.html'
  require => Package['nginx'],
}

exec { 'set_redirect':
  command => "sudo sed -i '\\#root /var/www/html;#a\\\\tlocation /red\
irect_me/ {\\n\\t\\treturn 301 https://www.youtube.com/watch?v=QH2-TG\
Ulwu4;\\n\\t}' /etc/nginx/sites-available/default",
  require => require => Package['nginx'],
}

exec {'HTTP header':
        command => 'sed -i "25i\        add_header X-Served-By \$host\
name;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

exec { 'restart nginx':
  command => 'sudo service nginx restart',
  require => Exec['set_redirect'],
}