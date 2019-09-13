all: .run

.ssh:
	mkdir -pv .ssh
	ssh-keygen -t rsa -f .ssh/id_rsa -N ""
	cp -v .ssh/id_rsa.pub .ssh/authorized_keys

.build: .ssh Dockerfile waiter.py setup.py myshell
	mkdir -pv bin
	-cp -v $(HOME)/bin/* bin
	docker build -f Dockerfile -t boom-image .
	touch .build

kill:
	-docker kill boom

.run: kill .build .ssh setup.py
	docker run --hostname boom --detach --name boom boom-image
	docker exec boom python /tmp/setup.py

	touch .run

ansible: kill .build .ssh setup.py gather_ips.py
	docker run --hostname boom --detach --name boom boom-image
	docker exec boom python /tmp/setup.py

clean: kill
	-docker rmi -f boom-image
	rm -frv .build .run .ssh bin
