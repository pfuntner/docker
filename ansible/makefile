all: .run

.ssh:
	mkdir .ssh
	ssh-keygen -t rsa -f .ssh/id_rsa -N ""
	cp .ssh/id_rsa.pub .ssh/authorized_keys

.build: .ssh Dockerfile-ansible Dockerfile-vanilla waiter.py setup.py
	docker build -f Dockerfile-ansible -t bruno_ansible .
	docker build -f Dockerfile-vanilla -t bruno_vanilla .
	touch .build

.kill:
	-docker kill ansible vanilla1 vanilla2
	-docker rm -f ansible vanilla1 vanilla2

.run: .kill .build .ssh setup.py gather_ips.py
	docker run --dns 8.8.8.8 --dns 8.8.4.4 --hostname ansible --detach --name ansible bruno_ansible
	docker run --dns 8.8.8.8 --dns 8.8.4.4 --hostname vanilla1 --detach --name vanilla1 bruno_vanilla
	docker run --dns 8.8.8.8 --dns 8.8.4.4 --hostname vanilla2 --detach --name vanilla2 bruno_vanilla

	python gather_ips.py

	docker cp ips.json ansible:/tmp/ips.json
	docker cp ips.json vanilla1:/tmp/ips.json
	docker cp ips.json vanilla2:/tmp/ips.json

	docker exec ansible python /tmp/setup.py
	docker exec vanilla1 python /tmp/setup.py
	docker exec vanilla2 python /tmp/setup.py

	touch .run
	@echo
	@echo "Now run (not from cygwin!): docker exec -it ansible bash"

clean: .kill
	-docker rmi -f bruno_ansible bruno_vanilla
	rm -frv .build .run .ssh ips.json
