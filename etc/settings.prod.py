ALLOWED_HOSTS = ['blog.exo.icu']
DEBUG = False
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
]
