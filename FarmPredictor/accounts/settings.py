TEMPLATES = [
  {
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [str(BASE_DIR.joinpath('templates'))], #추가
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
       'django.template.context_processors.debug',
       'django.template.context_processors.request',
       'django.contrib.auth.context_processors.auth',
       'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]