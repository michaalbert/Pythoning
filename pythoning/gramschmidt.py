import math

def default_scalar_prod(vector1, vector2):
	res = 0
	v = zip(vector1, vector2)
	for i in v:
		res += i[0]*i[1]
	return res
	
def norm(vector):
	return math.sqrt(default_scalar_prod(vector, vector))

def gramschmidt(vectors):
	#res: liste von listen(vektoren), erstes element wird schon gegeben
	res = [map(lambda x: x*(1/norm(vectors[0])), vectors[0])]
	del vectors[0]
	#zws: liste mit zwischenergebnissen: <v_k, v'_i>v'_i
	zws = []
	
	for v in vectors:
		for w in res:
			zws.append(map(lambda x: x*default_scalar_prod(v, w), w))
			
		#erzeugt v_k" = v_k - sum_i=1 ^k-1(<v_k, v'_i>v'_i)	
		for	z in zws:
			v = map(lambda x: x[0]-x[1], zip(v, z))
			
		#v_k' = 1/norm(v_k")*v_k"
		v = map(lambda x: x*(1/norm(v)), v)
		#v_k' res anfuegen
		res.append(v)
	return res
	

