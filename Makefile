serv:
	python3 manage.py runserver

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

dockerup:
	docker-compose up -d

shell:
	./manage.py shell

env:
	source env/bin/activate
