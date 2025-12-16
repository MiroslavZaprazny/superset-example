# taken from https://github.com/apache/superset/blob/master/docker/pythonpath_dev/superset_config.py

import os

from flask_appbuilder.security.manager import AUTH_OAUTH

DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG
THUMBNAIL_CACHE_CONFIG = CACHE_CONFIG

AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_ROLES_SYNC_AT_LOGIN = True

KEYCLOAK_URI = os.getenv("KEYCLOAK_URI")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

OAUTH_PROVIDERS = [
    # https://github.com/dpgaspar/Flask-AppBuilder/blob/release/5.0.2/flask_appbuilder/security/manager.py#L702
    # In order to inherit groups from keycloak we need to add "Group Membership" client scope mapper
    # with the name "groups" so that FAB can map it successfully
    {   
        "name": "keycloak",
        "icon": "fa-key",
        "token_key": "access_token",
        'remote_app': {
            'client_id': KEYCLOAK_CLIENT_ID,
            'client_secret': KEYCLOAK_CLIENT_SECRET,
            'client_kwargs': {
                "scope": "openid email profile"
            },
            "api_base_url": "http://keycloak:8080/realms/superset/protocol/",
            "access_token_url": "http://keycloak:8080/realms/superset/protocol/openid-connect/token",
            "authorize_url": "http://keycloak:8080/realms/superset/protocol/openid-connect/auth",
            'jwks_uri': 'http://keycloak:8080/realms/superset/protocol/openid-connect/certs',
        },
    }
]

AUTH_ROLES_MAPPING = {
    "superset_admin": ["Admin"],
}

