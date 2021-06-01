# void-time

http://lyubosumaz.pythonanywhere.com/

## Build Setup

```
conda create --name myDjangoEnv django
conda info --envs
conda activate myDjangoEnv
python3 manage.py runserver

conda deactivate
```

```
DB
conda activate myDjangoEnv
python3 manage.py migrate
python3 manage.py makemigrations first_app
python3 manage.py migrate
python3 manage.py shell
from first_app.models import Topic
print(Topic.objects.all())
t = Topic(top_name="Social Network")
t.save()
print(Topic.objects.all())

python3 manage.py createsuperuser

```

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).
