# import PySimpleGUI
import PySimpleGUI as sg
  
  
# Choose a Theme for the Layout
sg.theme('DarkPurple7')
  
layout = [[sg.Text('Lista de Temas InBuild - PySimpleGui')],
          [sg.Text('Por favor escolha um Tema para uma Janela Demo')],
          [sg.Listbox(values = sg.theme_list(),
                      size =(20, 12),
                      key ='-LIST-',
                      enable_events = True)],
          [sg.Button('Exit')]]
  
window = sg.Window('Lista de Temas - PySimplyGui', layout)
  
# This is an Event Loop
while True:  
    event, values = window.read()
      
    if event in (None, 'Sair'):
        break
          
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
      
# Close
window.close()