build:
	docker build . -t elibrary
run:
	docker run -d -p 8000:8000 --rm --name elibrary elibrary
stop:
	docker stop elibrary