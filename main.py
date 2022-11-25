import PySimpleGUI as sg


def tela_inicial():
    layout = [
        [sg.Text('\n\tTELA DE CADASTRO\t')],
        [sg.Text('nome')],
        [sg.Input(key='nome')],
        [sg.Text('', key='msgN')],
        [sg.Text('sobrenome')],
        [sg.Input(key='sobrenome')],
        [sg.Text('', key='msgSN')],
        [sg.Text('e-mail')],
        [sg.Input(key='e-mail')],
        [sg.Text('', key='msgE-M')],
        [sg.Text('senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Text('', key='msgS')],
        [sg.Text('confirmar senha')],
        [sg.Input(key='confirmar senha', password_char='*')],
        [sg.Text('', key='msgCS')],
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
            window['msgN'].update('o campo nome deve ser preenchido')
        else:
            window['msgN'].update('')
        if valores['sobrenome'] == '':
            window['msgSN'].update('o campo sobrenome deve ser preenchido')
        else:
            window['msgSN'].update('')
        if valores['e-mail'] == '':
            window['msgE-M'].update('o campo e-mail deve ser preenchido')
        else:
            window['msgE-M'].update('')
        if valores['senha'] == '':
            window['msgS'].update('o campo senha deve ser preenchido')
        else:
            window['msgS'].update('')
        if valores['confirmar senha'] == '':
            window['msgCS'].update(
                'o campo confirmar senha deve ser preenchido')
        else:
            window['msgCS'].update('')
        if valores['senha'] != valores['confirmar senha']:
            window['msgCS'].update('as senhas devem ser iguais')
        else:
            window['msgCS'].update('')
