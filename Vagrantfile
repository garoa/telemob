# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "shell", path: "provisioner.sh", privileged: false
  config.vm.network :forwarded_port, guest: 8000, host: 8000
end
