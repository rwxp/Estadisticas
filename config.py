class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/etl-estadisticas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Otras configuraciones para producción

# Selecciona la configuración según el entorno de la aplicación
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
