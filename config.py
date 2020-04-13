import logging
import os


class Config(object):
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = logging.INFO


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG
