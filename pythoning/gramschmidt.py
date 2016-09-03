import math
#vectors are implemented as lists here

def default_scalar_prod(vector1, vector2):
	"""Calculates the default scalar product of two vectors."""
	res = 0
	v = zip(vector1, vector2)
	for i in v:
		res += i[0]*i[1]
	return res
	
def norm(vector):
	"""Calculates the Euclidean norm of a vector."""
	return math.sqrt(default_scalar_prod(vector, vector))

def gramschmidt(vectors):
	"""Orthonormalizes a set of vectors using the Gram-Schmidt-process."""
	res = [map(lambda x: x*(1/norm(vectors[0])), vectors[0])]
	del vectors[0]
	zws = []
	
	for v in vectors:
		for w in res:
			zws.append(map(lambda x: x*default_scalar_prod(v, w), w))	
		for	z in zws:
			v = map(lambda x: x[0]-x[1], zip(v, z))
		v = map(lambda x: x*(1/norm(v)), v)
		res.append(v)
	return res
