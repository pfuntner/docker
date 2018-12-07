all: .run

.build: Dockerfile
	docker build -t bruno_ansible .
	touch .build

.kill:
	-docker kill ansible
	-docker rm ansible

.run: .kill .build
	docker run --detach --name ansible bruno_ansible
	touch .run
	@echo
	@echo "Now run (not from cygwin!): docker exec -it ansible bash"

clean: .kill
	-docker rmi -f bruno_ansible
	rm -fv .build .run
