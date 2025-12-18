# taken from https://github.com/apache/superset/blob/master/docker/pythonpath_dev/superset_config.py

import os

from flask_appbuilder.security.manager import AUTH_OAUTH

SQLALCHEMY_DATABASE_URI = os.getenv("META_DATABASE_URI")

FEATURE_FLAGS = {
    'DASHBOARD_RBAC': True
}

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
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
FILTER_STATE_CACHE_CONFIG = CACHE_CONFIG
EXPLORE_FORM_DATA_CACHE_CONFIG = CACHE_CONFIG

AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_ROLES_SYNC_AT_LOGIN = True

KEYCLOAK_BASE_URI = os.getenv("KEYCLOAK_BASE_URI")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

OAUTH_PROVIDERS = [
    # https://github.com/dpgaspar/Flask-AppBuilder/blob/release/5.0.2/flask_appbuilder/security/manager.py#L702
    # In order to inherit groups/roles from keycloak out of the box there needs to be a "group" token claim sent 
    # in the user info endpoint. In keycloak this can be achieved using Mappers.
    {   
        "name": "keycloak",
        "icon": "fa-key",
        "token_key": "access_token",
        "remote_app": {
            "client_id": KEYCLOAK_CLIENT_ID,
            "client_secret": KEYCLOAK_CLIENT_SECRET,
            "client_kwargs": {
                "scope": "openid email profile"
            },
            "api_base_url": f"{KEYCLOAK_BASE_URI}/realms/{KEYCLOAK_REALM}/protocol/",
            "access_token_url": f"{KEYCLOAK_BASE_URI}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token",
            "authorize_url": f"{KEYCLOAK_BASE_URI}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth",
            "jwks_uri": f"{KEYCLOAK_BASE_URI}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/certs",
        },
    }
]

AUTH_ROLES_MAPPING = {
    "superset_admin": ["Admin"],
}

