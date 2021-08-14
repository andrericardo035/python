# Conversão de segundos

segundos = int(input('Digite a quantidade de segundos\n'))

# Divisão com retorno inteiro é //
# Divisão com retorno decimal é /

horas = segundos // 3600
segundos_restantes_aux = segundos % 3600
minutos = segundos_restantes_aux // 60
segundos_restantes = segundos_restantes_aux % 60

print(segundos, 'Segundos dá um total de', horas, 'horas', minutos, 'minutos e', segundos_restantes, 'segundos...')
