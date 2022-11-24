import PySimpleGUI as sg


def tela_inicial():
    layout = [
        [sg.Text('\n\tTELA DE CADASTRO\t')],
        [sg.Text('nome')],
        [sg.Input(key='nome')],
        [sg.Text('sobrenome')],
        [sg.Input(key='sobrenome')],
        [sg.Text('e-mail')],
        [sg.Input(key='e-mail')],
        [sg.Text('senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Text('confirmar senha')],
        [sg.Input(key='confirmar senha', password_char='*')],
        [sg.Button('cadastrar')],
        [sg.Text('', key='msg')]
    ]
    return sg.Window('cadastro', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
    if window == telaInicial and eventos == 'cadastrar':
        if valores['nome'] == '':
            print('o campo nome deve ser preenchido')
        if valores['sobrenome'] == '':
            print('o campo sobrenome deve ser preenchido')
        if valores['e-mail'] == '':
            print('o campo e-mail deve ser preenchido')
        if valores['senha'] == '':
            print('o campo senha deve ser preenchido')
        if valores['confirmar senha'] == '':
            print('o campo confirmar senha deve ser preenchido')
        if valores['senha'] != valores['confirmar senha']:
            print('as senhas devem ser iguais')
