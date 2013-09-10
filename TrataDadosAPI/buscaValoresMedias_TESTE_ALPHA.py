valores_RSSI={}
#Valores_RSSI  {'BSSI1': ('ESSID1', {(0, 1): [-40,-50,-50], (0, 2): [-40,-50,-50]})}
#Valores_RSSI  {'BSSI1': ('ESSID1', NOME)}
#Valores_RSSI  dict {'BSSID'}
#                       [0] : 'ESSID'
#                       [1] : {(position):valores}
#
#                                  BSSI  Pos   XY    Power DBM
#                   valores_RSSI["BSSI1"][1][(0,2)] = -30
#
#                                  BSSI  ESSID   nome
#                   valores_RSSI["BSSI1"][0]  = eduroam
#PARA ROTATIVIDADE VALOR DE POSICAO x=TEMPO y = 0
#
#


def addValue(bssi, essid, position, valores):
    if not valores_RSSI.has_key(bssi):
        valores_RSSI[bssi]=[]
        valores_RSSI[bssi].append("Nao apontei")
        valores_RSSI[bssi].append({})
    valores_RSSI[bssi][1][position] = valores
    
def busca_Valores_Rotatividade(fileCSV):
    with open(fileCSV) as infile:
        for line in infile:
            if not 'Saving Info at' in line:
                linha = line.strip().split(",")
                essid = linha[0]
                bssi = linha[1]
                position = (float(linha[3]),int(linha[2]))
                valores = int( linha[4])
                print str(bssi)+str(essid)+str(position)+str(valores)
                
                addValue(bssi, essid, position, valores)
       

def busca_Valores_WalkAndMesure(fileCSV):
    with open(fileCSV) as infile:
        for line in infile:
            linha = line.strip().split(",")
            essid = linha[2]
            bssi = linha[2]
            position = (int(linha[0]),int(linha[1]))
            valores = map(int, linha[3:])
            print str(bssi)+str(essid)+str(position)+str(valores)
            
            addValue(bssi, essid, position, valores)
   



def init_busca_Valores(fileCSV):
   if 'Rotatividade' in fileCSV:
        busca_Valores_Rotatividade(fileCSV)
   else: 
        busca_Valores_WalkAndMesure(fileCSV)     
            

if __name__ == '__main__':
    import os
    #init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\TESTE-ALPHA\\walkAndMesure2-LOG-TESTE-ALPHA-FULL.csv')
    init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\TESTE-ALPHA\\RealTime-Scan-Medicao-Rotatividade.csv')
    print "cenas"