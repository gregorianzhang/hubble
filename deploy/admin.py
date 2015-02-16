from django.contrib import admin

# Register your models here.

from deploy.models import server
admin.site.register(server)
from deploy.models import docker_images
admin.site.register(docker_images)
from deploy.models import docker_containers
admin.site.register(docker_containers)
