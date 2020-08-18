def resolve_sistema(m):
	def gauss(m):
		print("Operaçoes:")
		aux = m.copy()
		n = len(m)
		for d in range(n):
			if m[d][d] == 0:
				for i in range(n):
					if m[i][d] != 0:
						m[d], m[i] = m[i], m[d]
						break
				else:
					raise "Coluna igual a zero"
			for i in range(d+1, n):
				# m[i][d] + C * m[d][d] = 0
				c = - m[i][d] / m[d][d]
				print(f"L{i} = L{i} {c:+} * L{d}")
				for j in range(n+1):
					m[i][j] = m[i][j] + c * m[d][j]
		return aux

	def resolve(m):
		# matriz escalonada
		n = len(m)
		r = [0 for i in range(n)]
		for i in range(n-1, -1, -1):
			soma = 0
			for j in range(i+1, n):
				soma += r[j] * m[i][j]
			#calcula o valor da variavel
			r[i] = (m[i][n]-soma)/m[i][i]
		return r
		
	m_escalonada = gauss(m)
	return resolve(m_escalonada)

ms = [[
		[4, 1, 1, 6], 
		[2, 5, 2, 3],
		[1, 2, 4, 11]
	], [
		[3, 2, 1, 2],
		[2, 7, 2, -3],
		[1, 3, 5, 3]
	], [
		[1, 2, -3, 5],
		[0, -2, 1, -3],
		[-4, 1, -1, -2]
	], [
		[3, 1, 1, 1],
		[1, -4, 2, 3],
		[1, -3, 5, -1]
	]]

for i in range(len(ms)):
	print(f"### Questão {i+1}:")
	cof = resolve_sistema(ms[i])
	print("Solução =", cof)
	print()