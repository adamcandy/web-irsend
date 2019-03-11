
update:
	cat lircd.conf | sudo tee /etc/lirc/lircd.conf

archive:
	cd ~/; rm -f /tmp/web-irsend.tar.bz2; tar cjpf /tmp/web-irsend.tar.bz2 web-irsend; tar cjpf /tmp/berryhome.tar.bz2 ~/; cd -
	scp -rp /tmp/web-irsend.tar.bz2 /tmp/berryhome.tar.bz2 a:"lib/project/raspberry\ remote/"

commit: update archive
	git commit -a
	git push

restart:
	sudo /etc/init.d/lirc restart
	./daemon reset

