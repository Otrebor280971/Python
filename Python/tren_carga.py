def cargamentos(num_vagones, capacidades_vagones, num_cargamentos, capacidades_cargamentos):
    vagones = list(capacidades_vagones)

    
    for i in range(num_cargamentos):
        cargamento_actual = capacidades_cargamentos[i]
        for j in range(num_vagones):
            if vagones[j] >= cargamento_actual:
                vagones[j] -= cargamento_actual
                break

    return vagones


num_vagones = int(input())
capacidades_vagones = []
for _ in range(num_vagones):
    capacidad = int(input())
    capacidades_vagones.append(capacidad)


num_cargamentos = int(input())
capacidades_cargamentos = []
for _ in range(num_cargamentos):
    capacidad_cargamento = int(input())
    capacidades_cargamentos.append(capacidad_cargamento)

capacidades_restantes = cargamentos(num_vagones, capacidades_vagones, num_cargamentos, capacidades_cargamentos)

print(capacidades_restantes)