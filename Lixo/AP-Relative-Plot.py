import  TrataDadosAPI.buscaValoresMedias as buscaValoresMedias
import numpy
import API.AccessPoint as AP
import API.PhysicalAccessPoint as APF


APFisicos = APF.PhysicalAccessPoint()




def criaAP(bssi,bssi_name):
    
    global APFisicos
    
    apTemp = AP.AccessPoint(bssi_name, bssi[0])
    for position in bssi[1]:
        apTemp.addValues(position,bssi[1][position])
    APFisicos.insert(apTemp)
    
    return




def plotBSSID():
    import numpy as np
    import matplotlib.pyplot as plt
    from random import choice
    from matplotlib import cm
    import colorsys
    
    import matplotlib.gridspec as gridspec
    global APFisicos
    
    
    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1]) 

    ax = plt.subplot(gs[0])
    #plt.subplots_adjust(right=0.75)
    
    #Inicializa um contador de cores
    cor =0
    corArray={}
    plottedAPs={}
    axisPick = 0 #0 - Eixo X || 1 - Eixo Y
    
    #Inicializa o sitio para as anotacoes
    annotatePosition=0

    ax.axis([-12, 12,-90, 0])
  
    ax.set_ylabel('cenas')
    for bssi in APFisicos.getAPFisicoPerPiso(0,10):
     
        if axisPick == 0:
            positions = APFisicos.getPositions(bssi,rangeX=(-11,11),rangeY=(0,1))
        if axisPick == 1:
            positions = APFisicos.getPositions(bssi,rangeX=(0,1),rangeY=(-11,11))
        if positions:
            cor+=1
            corPick = cm.jet(1.*cor/len(APFisicos.getAPFisicoPerPiso(0,10)))
            corArray[APFisicos.getAPName(bssi)]=corPick
            plottedAPs[bssi] = APFisicos.getAPName(bssi)
            
            ax.plot( [ x[axisPick] for x in positions] #tira as posicoes X ou Y AXISPICK 
            , [ APFisicos.getAverage(bssi,x) for x in positions] #tira as avgs de cada posicao
            , color = corPick, linestyle='-', marker="o" , label = APFisicos.getLocation(bssi)+" Var: " )
            
            
            
            for position in positions:
 
                valueBSSI = round(APFisicos.getAverage(bssi,position),2)
                valueVariance = round(APFisicos.getVariance(bssi,position),2)
               
                
                if valueVariance :
                    ax.scatter(position[axisPick],valueBSSI,s=valueVariance*20)
                    ax.annotate("var:"+str(valueVariance),fontsize='xx-small', xy=(position[axisPick], valueBSSI), xytext=(position[axisPick]+0.1, valueBSSI-1.5) )
                
                ax.annotate(str(valueBSSI),fontsize='xx-small', xy=(position[0], valueBSSI), xytext=(position[axisPick]+0.1, valueBSSI+0.5) )
                annotatePosition +=1


    ax.legend(loc='upper left')
    ax2 = plt.subplot(gs[1])

    import matplotlib.image as mpimg
    from pylab import *
    import os
    img=mpimg.imread(os.path.dirname(__file__) + '\\_Tratamento de Dados\\piso0-tagus.png')
    imgplot1 = ax2.imshow(img)
    #ax2.autoscale_view('tight')
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)
    
    for bssi in plottedAPs:
        
        AP_rect = Rectangle(APFisicos.getLocMap(bssi), 20, 20, facecolor=corArray[plottedAPs[bssi]], edgecolor='black')
        ax2.add_patch(AP_rect)
        AP_linha =  Line2D([240, APFisicos.getLocMap(bssi)[0]], [327, APFisicos.getLocMap(bssi)[1]], lw=2, color=corArray[plottedAPs[bssi]], axes=ax,linestyle='--',linewidth=1000,solid_capstyle="round")
        ax2.add_line(AP_linha)

    
    if axisPick == 0:
        medicao_line = Line2D([240, 250], [327, 365], lw=2, color='green', axes=ax,linestyle='-',linewidth=1000,solid_capstyle="round")
    else:
        medicao_line = Line2D([186, 291], [345, 311], lw=2, color='green', axes=ax,linestyle='-',linewidth=1000,solid_capstyle="round")
    ax2.add_line(medicao_line)
 
   
    plt.subplots_adjust(hspace = .001,wspace = 0.02,bottom = 0.01,top = 0.1,left  = 0, right=0.1)
    plt.tight_layout()

    plt.show()
    #plt.savefig('Medidas-Relative-plot.png')
    return





if __name__ == '__main__':
    #buscar os valors do dblistings
    #cria apBSSID e AP Fisico
   
    #fazer o plot da lista
    import os.path
    
    buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\_Tratamento de Dados\\listings_dbm_final-FINAL.csv')
    for bssi in buscaValoresMedias.valores_RSSI:
        criaAP(buscaValoresMedias.valores_RSSI[bssi],bssi)

    
    plotBSSID()
    
def renderedRelativePlot():
    buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\_Tratamento de Dados\\listings_dbm_final-FINAL.csv')
    for bssi in buscaValoresMedias.valores_RSSI:
        criaAP(buscaValoresMedias.valores_RSSI[bssi],bssi)

    
    plotBSSID()
