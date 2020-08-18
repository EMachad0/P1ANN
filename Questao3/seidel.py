def jacobi(m, chute, n=10):
    # ex:
    # 4x+y+z=6 --> x = (6 - y - z) / 4
    # 2x+5y+2z=3 --> y = (3 - 2x - 2z) / 5
    # x+2y+4z=11 --> z = (11 - x - 2y) / 4
    
    ci = chute.copy()
    itr = [ci.copy()]
    for i in range(1, n+1):
        for j, row in enumerate(m):
            subs = sum([el * ci[k] for k, el in enumerate(row[:-1]) if k != j])
            subs = (row[-1] - subs) / row[j]
            ci[j] = subs
        itr.append(ci.copy())

    return itr

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
    chute = [0] * len(ms[i])
    itr = jacobi(ms[i], chute)
    print(f"Método de Seidel com chute inicial =", chute)
    print("|itr | x | y | z|")
    print("|----|---|---|--|")
    for j, r in enumerate(itr):
        x, y, z = r
        print(f"|{j}| {x}| {y}| {z}|")
    print()