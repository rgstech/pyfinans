#coding: utf-8
#Pyfinans V2 
#Script desenvolvido por Rodrigo Guimaraes
#github: rgtech
#Controle simples de despesas pessoais
#Made and tested with python version : 3.11.9
#License: MIT

try:

    import os
    import sys
    import time
    import datetime
    import csv
    from openpyxl    import Workbook #lib para excel
    from prettytable import PrettyTable

except ImportError:
    
    print("Erro! Faltando bibliotecas de codigo")     
    
    
    
def save_record(reg):
    
   if os.path.exists('financeiro.csv'):
       with open('financeiro.csv', 'a', newline='') as file:
           writer = csv.writer(file, delimiter=';')
           writer.writerow(reg)
   return None    
    
                  
            
def read_file(filename):
    
    # lendo csv file
    if os.path.exists(filename):    
        with open(filename, 'r') as csvfile:
            # criando um csv reader object 
            csvreader = csv.reader(csvfile, delimiter=';')    
            return list(csvreader)
    return None



def excel_export(): # exporta dados para excel / exports data to excel file 
     
    lregs  = read_file('financeiro.csv') #lregs = lista de registros
    
    book = Workbook()

    sheet = book.active

    print("**** Informe a data inicial **** ")
    dt_start = get_date()
    print("**** Informe a data final **** ")
    dt_end = get_date()

    for row in lregs:
        str_date = row[3]
        rowdate = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
        if rowdate >= dt_start and rowdate <= dt_end: #verifica se a data da linha corrente no loop esta entre as datas escolhidas
           sheet.append(row)

    book.save('exportado_finans.xlsx')

    pause_screen("Exportado com sucesso!")
    


def op_lancar():
    
    reg = menu_entrada_lancar()
    save_record(reg)
    pause_screen("\n*** REGISTRO SALVO COM SUCESSO! ***")
   


def op_desp_ano():
    
    now = datetime.datetime.now()
    
    with open('financeiro.csv', 'r') as csvfile:
         rows = [] # filtrar jogando apenas o ano 
         csvreader = csv.reader(csvfile, delimiter=';')    
         # extraindo cada linha, uma por uma 
         for row in csvreader:
             str_date = row[3]
             date = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
             if now.year == date.year: #compara ano de hoje com o ano da linha corrente no loop
                 rows.append(row) 
         msum = 0
         if rows:
             for row in rows:
                 msum += float(row[2])
         print(f"O total de despesas desse ano foi de R$ {msum:.2f}")
         pause_screen()
    

 
def op_desp_mes():
    
    now = datetime.datetime.now()
    
    with open('financeiro.csv', 'r') as csvfile:
         rows = [] # filtrar jogando apenas o mes 
         csvreader = csv.reader(csvfile, delimiter=';')    
         # extraindo cada linha, uma por uma 
         for row in csvreader:
             str_date = row[3]
             date = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
             if now.month == date.month: #compara mes de hoje com o mes da linha corrente no loop
                 rows.append(row) 
         msum = 0
         if rows:
             for row in rows:
                 msum += float(row[2])
         print(f"O total de despesas desse mês foi de R$ {msum:.2f}")
         pause_screen()
         
         
                  
def op_desp_semana(): 

     now = datetime.datetime.now() # pega data de hoje
     nweek = now.isocalendar()[1] # pega o numero da semana atual
     rows = [] # lista filtrada pelo numero da semana 
     with open('financeiro.csv', 'r') as csvfile:
         csvreader = csv.reader(csvfile, delimiter=';')  
         for row in csvreader:
             str_date = row[3]
             date = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
             nweekreg = datetime.date(date.year,date.month, date.day).isocalendar()[1]
             if nweek == nweekreg:  #compara numero da semana atual com o numero da semana da linha corrente
                 rows.append(row) 
         ssum = 0
         if rows:
             for row in rows:
                 ssum += float(row[2])
         print(f"O total de despesas dessa semana foi de R$ {ssum:.2f}")
         pause_screen()
         

         
def op_desp_dia():
    
    now = datetime.datetime.now()
    str_today_date = time.strftime("%d/%m/%Y")
    today_date = datetime.datetime.strptime(str_today_date, '%d/%m/%Y').date() # data de hoje em formato dd/mm/yyyy
    with open('financeiro.csv', 'r') as csvfile:
         rows = [] # filtrar jogando apenas o do dia
         csvreader = csv.reader(csvfile, delimiter=';')    
         # extraindo cada linha, uma por uma 
         for row in csvreader:
             str_date = row[3]
             rowdate = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
             if today_date == rowdate: #compara dia de hoje com o dia da linha corrente no loop
                 rows.append(row) 
         dsum = 0
         if rows:
             for row in rows:
                 dsum += float(row[2])
         print(f"O Total de despesas do dia foi de R$ {dsum:.2f}")
         pause_screen()
    

            
def op_desp_data():
    
    print("*** Informe a Data ***")
    dt_val = get_date()
    with open('financeiro.csv', 'r') as csvfile:
         rows = [] # filtrar jogando apenas a  linha com a data escolhida 
         csvreader = csv.reader(csvfile, delimiter=';')    
         # extraindo cada linha, uma por uma 
         for row in csvreader:
             str_date = row[3]
             rowdate = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
             
             if dt_val == rowdate: #compara data escolhida com a data da linha corrente no loop
                 rows.append(row) 
         dsum = 0
         if rows:
             for row in rows:
                 dsum += float(row[2])
         print(f"O total de despesas da data escolhida foi de R$ {dsum:.2f}")
         pause_screen()



def op_desp_data_faixa():
    
    print("**** Informe a data inicial **** ")
    dt_start = get_date()
    print("**** Informe a data final **** ")
    dt_end = get_date()
    with open('financeiro.csv', 'r') as csvfile:
         rows = [] # filtrar jogando apenas a  linha com a data escolhida 
         csvreader = csv.reader(csvfile, delimiter=';')    
         # extraindo cada linha, uma por uma 
         for row in csvreader:
             str_date = row[3]
             rowdate = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
             if  rowdate >= dt_start and rowdate <= dt_end: #verifica se a data da linha corrente no loop esta entre as datas escolhidas
                 rows.append(row) 
         dsum = 0
         if rows:
             for row in rows:
                 dsum += float(row[2])
        #print(f"total de despesas entre {dtstr_start}  a {dtstr_end}  foi de {dsum:.2f}")
         print(f"O total de despesas entre as datas escolhidas foi de R$ {dsum:.2f}")
         pause_screen()



def op_media_desp(dtopt = None): #função multiuso/generica para calculo da média
     
    lregs  = read_file('financeiro.csv')    
    now = datetime.datetime.now() #full date time
    str_today_date = time.strftime("%d/%m/%Y")
    today_date = datetime.datetime.strptime(str_today_date, '%d/%m/%Y').date() # data de hoje em formato dd/mm/yyyy
    rows = [] # filtrar jogando apenas o ano
    vflag = False 
    dt_espec_a = None
    dt_espec_b = None
    
    if dtopt == 'espec':
        print(" INFORME A DATA ESPECIFICA PARA VISUALIZAÇÃO: ")
        dt_espec_a = get_date() 
    elif dtopt == 'fespec':
        print(" INFORME A DATA DE INICIO: ")
        dt_espec_a = get_date() 
        print(" INFORME A DATA FINAL: ")
        dt_espec_b = get_date() 
                   
    for row in lregs:
        str_date = row[3]
        rowdate = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
        if not dtopt:
            return
        elif dtopt == 'espec':
            vflag = dt_espec_a == rowdate
        elif dtopt == 'fespec':
            vflag = rowdate >= dt_espec_a and rowdate <= dt_espec_b
        elif dtopt == 'today':
            vflag = today_date == rowdate
        elif dtopt == 'year':
            vflag = now.year == rowdate.year
        elif dtopt == 'month':
            vflag = now.month == rowdate.month
        elif dtopt == 'week':
                nweekreg = datetime.date(rowdate.year, rowdate.month, rowdate.day).isocalendar()[1]  # pega o numero da semana do registro
                nweek = now.isocalendar()[1] # pega o numero da semana atual
                vflag =  nweek == nweekreg
        if  vflag: #verifica os registros a incluir caso seja do periodo escolhido
            rows.append(row) 
    msum = 0
    if rows:
        for row in rows:
            msum += float(row[2])
    try:
        msum = msum / len(rows) 
        print(f"media de gastos do tempo informado e de = R$ {msum:.2f}")   
    except ZeroDivisionError:
        print("Erro, divisão por zero")
    pause_screen()
    

                     
def list_reg(listoption = 'all'):
    lregs  = read_file('financeiro.csv') # carrega os registros do arquivo e retorna como uma lista(tambem conhecido como array)

    if listoption == 'all':
        show_table(lregs)
        pause_screen()
        
    now = datetime.datetime.now()
    str_today_date = time.strftime("%d/%m/%Y")
    today_date = datetime.datetime.strptime(str_today_date, '%d/%m/%Y').date() # data de hoje em formato dd/mm/yyyy
    rows = [] # filtrar jogando apenas o ano
    vflag      = False 
    dt_espec_a = None
    dt_espec_b = None
    
         
    if listoption == 'espec': # espec data especifica
        print("*** INFORME A DATA ESPECIFICA PARA VISUALIZAÇÃO: \n***")
        dt_espec_a = get_date() 
    elif listoption == 'fespec': # fespec = faixa especifica
        print(" INFORME A DATA DE INICIO: ")
        dt_espec_a = get_date() 
        print(" INFORME A DATA FINAL: ")
        dt_espec_b = get_date() 
        
              
    for row in lregs:
        str_date = row[3]
        rowdate = datetime.datetime.strptime(str_date, '%d/%m/%Y').date() #converte a data string do formato dd/mm/aaa para aaaa-mm-dd(sistema)
        if not listoption:
             main()
        elif listoption == 'espec':
            vflag = dt_espec_a == rowdate
        elif listoption == 'fespec':
            vflag = rowdate >= dt_espec_a and rowdate <= dt_espec_b
        elif listoption == 'today':
            vflag = today_date == rowdate
        elif listoption == 'year':
            vflag = now.year == rowdate.year
        elif listoption == 'month':
            vflag = now.month == rowdate.month
        elif listoption == 'week':
            nweekreg = datetime.date(rowdate.year, rowdate.month, rowdate.day).isocalendar()[1]  # pega o numero da semana do registro
            nweek = now.isocalendar()[1] # pega o numero da semana atual
            vflag =  nweek == nweekreg
        
        if vflag: #verifica os registros a incluir caso seja do periodo escolhido
            rows.append(row)     
            
    show_table(rows)
    pause_screen()

    
    
def show_table(lregs = []):
    
    tbregs = PrettyTable()
    tbregs.field_names = ["CATEGORIA", "DESCRIÇÃO", "VALOR DA DESPESA", "DATA"]
    if lregs:
        for reg in lregs:
            tbregs.add_row([reg[0], reg[1], f"R$ {reg[2]}", reg[3]])
        print(tbregs) #imprime todos os registros em forma de tabela usando o PrettyTable
    else:
        print("\n\n**** NÃO HÁ REGISTROS A SEREM EXIBIDOS ****\n\n")
    

    
def pause_screen(msg = None):
    if msg:
        print(msg)
    input("\n APERTE QUALQUER TECLA PARA CONTINUAR... ")
    main()


    
def get_date(str=False): #pega do usuario a data em string e retorna convertida ou em formato string dependendo da flag 'str'
     
     print("Digite o dia(numero)")
     dt_d = input('')
     print("Digite o mes(numero)")
     dt_m = input('')
     print("Digite o ano(numero)")
     dt_a = input('')
     
     dt_full = dt_d+'/'+dt_m+'/'+dt_a
     if str:
         return dt_full        
     else:
         vdate = datetime.datetime.strptime(dt_full, '%d/%m/%Y').date()
         return vdate
    

       
def menu_entrada_lancar():
    
    lrow = []
    print("Digite a categoria")
    lrow.append(input(''))
    print("Digite a descricao da despesa, ex: 'dois paes e 1 caixa de leite'")
    lrow.append(input(''))
    print("Digite o valor total da despesa")
    lrow.append(input(''))
    print("Digite a data em que ocorreu a despesa no formato dd/mm/aaaa")
    lrow.append(input(''))

    return lrow



def create_menu(menu_title = "", moptions = {}): # criar menu dinamicamente passando titulo e as opçoes em um dicionario
    
    if menu_title:
        print(f"\n ***** {menu_title} ***** \n")
    if moptions:
        for op, msg in moptions.items():
            print(f"({op}) - {msg}")
        return input('>> ')
 

 
def main(): # funcao principal
    
    op = ''
    menu_title    =   "DIGITE A LETRA DA OPERAÇAO DESEJADA E PRESSIONE <ENTER>"
    menu_options  = { "l" : "Lançar Despesa \n",
                      "d" : "Calcular total de despesa do dia\n",
                      "s" : "Calcular total de despesa da semana\n",
                      "m" : "Calcular total de despesa do mes atual\n",
                      "a" : "Calcular total de despesa do ano atual\n",
                      "e" : "Calcular total de despesa numa data especifica\n", 
                      "f" : "Calcular total de despesa numa faixa de tempo especifica\n",
                      "u" : "Calcular gasto médio de hoje\n", 
                      "k" : "Calcular gasto médio do ano atual\n", 
                      "v" : "Calcular gasto médio do mês atual\n", 
                      "j" : "Calcular gasto médio da semana atual\n", 
                      "b" : "Calcular gasto médio de uma data especifica\n", 
                      "h" : "Calcular gasto médio numa faixa de tempo especifica\n", 
                      "r" : "Ver todos registros\n",
                      "t" : "Ver todos os registros de hoje\n",    
                      "o" : "Ver todos os registros do ano atual\n",    
                      "i" : "Ver todos os registros do mes atual\n",   
                      "n" : "Ver todos os registros da semana atual\n", 
                      "z" : "Ver registros de uma data especifica\n",  
                      "g" : "Ver registros numa faixa de tempo especifica\n",
                      "x" : "########## Exportar todos registros para EXCEL (backup) ########## \n",  
                      "q" : "Sair do programa \n" }
    
    op = create_menu(menu_title, menu_options)
    
    
    while op != 'q':
        if op == 'l': 
            op_lancar()
        elif op == 's':
            op_desp_semana()    
        elif op == 'd':
            op_desp_dia()
        elif op == 'm':
            op_desp_mes()
        elif op == 'a':
            op_desp_ano()
        elif op == 'e':
            op_desp_data()
        elif op == 'f':
            op_desp_data_faixa()
        elif op == 'u':
            op_media_desp('today')
        elif op == 'k':
            op_media_desp('year')
        elif op == 'v':
            op_media_desp('month')
        elif op == 'j':
            op_media_desp('week')
        elif op == 'b':
            op_media_desp('espec')
        elif op == 'h':
            op_media_desp('fespec')
        elif op == 'r':
            list_reg()
        elif op == 't':
            list_reg('today')
        elif op == 'o':
            list_reg('year')
        elif op == 'i':
            list_reg('month')
        elif op == 'n':
            list_reg('week')
        elif op == 'z':
            list_reg('espec')
        elif op == 'g':
            list_reg('fespec')
        elif op == 'x':
            excel_export()                 
        else:
            print("Opçao invalida. Tente novamente\n")
            main()
    print("\n\nVOCE FINALIZOU O PROGRAMA COM SUCESSO! ATE BREVE! \n")
    sys.exit(1)
           
                                                                        
if __name__ == "__main__":
    main() 

  
