import importlib

def readKOD (f):
    extension = f.split('.')
    if extension[-1] == 'py':
        compillPyhon(f)
    elif extension[-1] == 'go':
        compillGO(f)
    elif extension[-1] == 'java':
        compillJava(f)
def compillPyhon (p):
    importlib.import_module(p)

def compillGO (g):
    print('тут мы собираем ГО')

def compillJava (j):
    print('тут мы собираем джаву')

readKOD(input('Введите путь к файлу'))
