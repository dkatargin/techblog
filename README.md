Just simple blog with **django** and **react** :) 

# Deployment with docker
First of all you need make db.sqlite3 with superuser account
```bash
$ python3 makemigrations
$ python3 migrate
$ python3 createsuperuser
```
next step is docker deploy
```bash
$ docker-compose build && docker-compose up -d
```
after this you get nginx service on 80 port

# Manage posts
You can add/modify/delete posts over django-admin(/admin)

# Todo list
| Feature        | Status       |
| ------------- |:-------------:|
| Initial DB models     |  **OK** |
| Initial API for posts |  **OK** |
| Initial styles        |  **OK** |
| Initial react-screens |  **OK** |
| Add global variables to js-config  |  **OK**  |
| Main screen pagination             |  **OK** |
| Replace react default icons        |  **OK** |
| Add webpack build                  |  **OK** |
| Deployment with docker             | **OK** |
| Extended editor for posts          | WIP |
| Post Tags                          | WIP |
| Posts calendar                     | WIP |
| Mobile view                        | WIP |
| SEO improvements                   | WIP |
| Comments                           | WIP |
