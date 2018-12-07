all: .run

.build: Dockerfile waiter.py
	docker build -t bruno_ansible .
	touch .build

.kill:
	-docker kill ansible
	-docker rm -f ansible

.run: .kill .build
	docker run --dns 8.8.8.8 --dns 8.8.4.4  --detach --name ansible bruno_ansible
	touch .run
	@echo
	@echo "Now run (not from cygwin!): docker exec -it ansible bash"

clean: .kill
	-docker rmi -f bruno_ansible
	rm -fv .build .run
