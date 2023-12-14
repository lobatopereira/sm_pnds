from funsionariu.models import *


def c_user_fun(user):
	objects = Funsionariu.objects.filter(userFunsionariu__user=user).prefetch_related('userFunsionariu').first()
	fun = ""
	if objects:
		fun = objects
	return fun