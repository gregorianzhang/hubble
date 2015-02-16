from django.db import models

# Create your models here.

class server(models.Model):
    internet = models.GenericIPAddressField(protocol='IPv4',blank=True, null=True, unique=True, default=None)
    intranet = models.GenericIPAddressField(protocol='IPv4',blank=True, null=True, unique=True, default=None)
    mac_address = models.CharField(max_length=17, blank=True, null=True, unique=True, default=None)
    host_name = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)
    cpu_info = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    memory_info = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    disk_info = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)

    def __str__(self):
        return u'%s' % (self.host_name)

class docker_images(models.Model):
    repository = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)
    tag = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)
    image_id = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)
    created = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    size = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)

    def __str__(self):
        return u'%s' % (self.repository)

class docker_containers(models.Model):
    containter_id = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)
    image = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)
    command = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    created = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    status = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    ports = models.CharField(max_length=255, blank=True, null=True, unique=False, default=None)
    names = models.CharField(max_length=255, blank=True, null=True, unique=True, default=None)

    def __str__(self):
        return u'%s' % (self.containter_id)

