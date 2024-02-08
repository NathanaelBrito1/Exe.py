#média de três notas determinando se o aluno foi aprovado (média >= 7) ou reprovado (média < 7).

nota1 = 8
nota2 = 7
nota3 = 4
notaFinal = (nota1 + nota2 + nota3)/2
if notaFinal >= 7:
    print(notaFinal, "Parabéns! Você está aprovado!")
else:
    print(notaFinal, "Não desista! Você é capaz!")