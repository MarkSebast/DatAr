import matplotlib.pyplot as plt
import pandas

colnames = [
            "uno", "dos", "tres", "cuatro", "cinco", "seis"
            ]
data = pandas.read_csv('reservas bcra.csv', names=colnames, sep=';')

ano = data.uno.tolist()
mes = data.dos.tolist()
reservas = data.seis.tolist()

ano_mes = [i + j for i, j in zip(ano, mes)]


ano_mes.pop(0)
reservas.pop(0)


plt.plot(ano_mes, reservas)
plt.xlabel('mes')
plt.ylabel('reservas')
plt.title('Reservas BCRA x mes')
plt.legend()
plt.show()
