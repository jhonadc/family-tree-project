from logging import StreamHandler
import logging
import os
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Role
import psycopg2


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@classmethod
def init_app(cls, app):
    Config.init_app(app)
    # email errors to the administrators
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    secure = None
    if getattr(cls, 'MAIL_USERNAME', None) is not None:
        credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
        if getattr(cls, 'MAIL_USE_TLS', None):
            secure = ()
    mail_handler = SMTPHandler(
        mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
        fromaddr=cls.FLASKY_MAIL_SENDER,
        toaddrs=[cls.FLASKY_MAIL_SENDER],
        subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
        credentials=credentials,
        secure=secure)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()
