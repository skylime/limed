from celery.decorators import task
from subprocess import call
from celery.task.http import URL
import settings

@task
def list_base_images():
	return settings.CLOUD_BASE_IMAGES


@task(ignore_result=True)
def create_instance(base_image, name, instance, cpu_cores, memory, storage):
	# get ip
	# get ssh keys
	print call([
		'virt-clone',
		'--original', base_image,
		'--name', name,
		'--file',  settings.CLOUD_VM_DIR + '/' + name + '.qcow2'
	])
	# migrate to destination system

	URL(settings.CLOUD_ACTIVATE_URL).get_async(instance = instance, site_api_key = settings.SITE_API_KEY)
