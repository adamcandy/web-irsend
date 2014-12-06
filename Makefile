
update:
	cat lircd.conf | sudo tee /etc/lirc/lircd.conf

archive:
	cd ~/; rm -f ~/web-irsend.tar.bz2; tar cjpf web-irsend.tar.bz2 web-irsend; cd -
	scp -rp ~/web-irsend.tar.bz2 e:"/d/lib/project/raspberry\ remote/"

commit: update archive
	git commit -a
	git push

restart:
	sudo /etc/init.d/lirc restart
	./daemon reset

