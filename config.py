import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = false
    UPLOADED_RULES_DEST = ''
    UPLOADED_RULES_URL = ''
    UPLOADED_RULES_ALLOW = '.xml'
    
