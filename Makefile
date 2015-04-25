serve:
	@python manage.py 0.0.0.0:8000

test:
	@coverage run --source={{ project_name }}/ --omit=*/wsgi.py manage.py test
	@coverage report
	@coverage html
