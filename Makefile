
update:
	cat lircd.conf | sudo tee /etc/lirc/lircd.conf

archive:
	cd ~/; rm ~/web-irsend.tar.bz2; tar cjpf web-irsend.tar.bz2 web-irsend; cd -
