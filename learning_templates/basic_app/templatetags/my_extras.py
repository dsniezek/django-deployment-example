from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
	"""
	This function will cut 'arg' from a value(string)
	"""
	return value.replace(arg,'')

#register.filter('cut', cut)