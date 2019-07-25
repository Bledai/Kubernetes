Vagrant.configure("2") do |config|
  ip=["192.168.56.225"]
  box="sbeliakou/centos"
  servers=[
  {
    :hostname => "master",
    :ip => ip[0],
    :box => "sbeliakou/centos",
    :ram => 6072,
    :cpu => 2,
  }
]
    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|
            node.vm.box = machine[:box]
            node.vm.hostname = machine[:hostname]
            node.vm.network "private_network", ip: machine[:ip]
            node.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", machine[:ram]] 
            end      
        end              
    end
end
