# README #

The code for a blog built using Wagtail located at https://blog.richardgiddings.co.uk/

This blog features:
- The use of Amazon S3 for hosting images
- The use of django-comments-xtd for comments on each post
- Pagination using django.core.paginator
- http://pygments.org/ is used for code formatting

and is setup to deploy to Heroku, with a postgres database.

The following environment variables need to be added for Amazon S3 storage:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME

To specify the settings file to use:
- DJANGO_SETTINGS_MODULE - set as howto_project.settings.production

For email functionality:
- DEFAULT_FROM_EMAIL
- EMAIL_HOST
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- EMAIL_PORT

And finally:
- SECRET_KEY