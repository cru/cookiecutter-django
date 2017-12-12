import os, sys

if __name__ == "__main__":
    proj_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # This is so Django knows where to find stuff.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    sys.path.append(proj_path)

    # This is so my local_settings.py gets loaded.
    os.chdir(proj_path)

    # This is so models get loaded.
    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()
