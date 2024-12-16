from django.apps import AppConfig


class RegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg'

import flask

registration = flask.Blueprint(
    name="registration",
    import_name="app",
    template_folder="registration/templates"
)
