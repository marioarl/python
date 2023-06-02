'''Crie um programa qye tenha funçao notas() que pode receber varias notas de alunos e vao retornar um dicionario com as informaçoes:
- Quantidade de notas / a maior nota / a media da turma / a situacao (opcional)
Adicione tambem as docstrings da funcao'''
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r



#programa principal
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
