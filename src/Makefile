user:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

up:
	python manage.py runserver

startapp:
	@read -p "Enter the name of the application: " app_name; \
	cd apps; \
	python ../manage.py startapp $$app_name; \
	cd ..

check:
	python manage.py makemigrations --dry-run --check