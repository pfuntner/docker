all: .run

.ssh:
	mkdir .ssh
	ssh-keygen -t rsa -f .ssh/id_rsa -N ""
	cp .ssh/id_rsa.pub .ssh/authorized_keys

.build: .ssh Dockerfile-ansible Dockerfile-vanilla waiter.py
	docker build -f Dockerfile-ansible -t bruno_ansible .
	docker build -f Dockerfile-vanilla -t bruno_vanilla .
	touch .build

.kill:
	-docker kill ansible vanilla1 vanilla2
	-docker rm -f ansible vanilla1 vanilla2

.run: .kill .build update_resolv_conf .ssh
	docker run --dns 8.8.8.8 --dns 8.8.4.4 --hostname ansible --detach --name ansible bruno_ansible
	docker run --dns 8.8.8.8 --dns 8.8.4.4 --hostname vanilla1 --detach --name vanilla1 bruno_vanilla
	docker run --dns 8.8.8.8 --dns 8.8.4.4 --hostname vanilla2 --detach --name vanilla2 bruno_vanilla

	./update_resolv_conf

	docker exec ansible ssh localhost -o StrictHostKeyChecking=no true
	docker exec ansible ssh ansible -o StrictHostKeyChecking=no true
	docker exec ansible ssh vanilla1 -o StrictHostKeyChecking=no true
	docker exec ansible ssh vanilla2 -o StrictHostKeyChecking=no true

	docker exec vanilla1 ssh localhost -o StrictHostKeyChecking=no true
	docker exec vanilla1 ssh ansible -o StrictHostKeyChecking=no true
	docker exec vanilla1 ssh vanilla1 -o StrictHostKeyChecking=no true
	docker exec vanilla1 ssh vanilla2 -o StrictHostKeyChecking=no true

	docker exec vanilla2 ssh localhost -o StrictHostKeyChecking=no true
	docker exec vanilla2 ssh ansible -o StrictHostKeyChecking=no true
	docker exec vanilla2 ssh vanilla1 -o StrictHostKeyChecking=no true
	docker exec vanilla2 ssh vanilla2 -o StrictHostKeyChecking=no true

	touch .run
	@echo
	@echo "Now run (not from cygwin!): docker exec -it ansible bash"

clean: .kill
	-docker rmi -f bruno_ansible bruno_vanilla
	rm -frv .build .run .ssh
