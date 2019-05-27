import matplotlib.pyplot as plt
import datetime as date

def grafic(temperatura):   
    dades = temperatura # Valors de les variables
    #dades2=humitat
    ind=range(10) # Coordenades x datos ejes x
    #graficos una fila y 2 columnas(subplots). Una figura dos graficos
    fig, (ax1) = plt.subplots(1,1) # Numero de grafiques que dibuixem a la figura. que passa si fem fig, (ax1,ax2) = plt.subplots(1,2)
    # Margins
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=1, hspace=None)
    
    ############################ DIAGRAMA DE BARRES HORITZONTAL###################################################################################
    width = 0.5 # Amplada de les barres dels diagrames
    #diagrama de barras
    rects1 = ax1.bar(ind, dades, width, color='r') # Dades dels diagrames. Coordenades, Valors de les variables, Amplada i Color.
    ax1.set_ylabel('Cuenta Personas') # Llegenda de eix Y.
    ax1.set_title('Contador') # Titol del grafic
    ax1.set_xticks(ind) # Marques sota de cada diagrama (___|___)
    ax1.yaxis.set_major_locator(plt.NullLocator())
    ax1.set_xticklabels(('10 minuto')) # Text sota de cada diagrama en aquest cas HOMES i DONES.
    ax1.set_yticklabels([])
   
    for rect in rects1: # Dibuixem cadascun dels diagrames que son rectangles.
        height = rect.get_height() # De cada rectangle agafem la seva alcada.
        ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom') # Els valors quedaran damunt del diagrama
        #ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom')
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)  


    ################################ GUARDAR LA FIGURA CREADA #################################################################
    
    nomArchiu = 'graficos/' + str(date.datetime.now()) + '.png'
    #sustituir los dos puntos por otro caracter
    nomArchiu = nomArchiu.replace(':','_')
    plt.savefig(nomArchiu, bbox_inches='tight')
    plt.close(fig)

#grafic([23,45,10,50,32,12,45,32,5,17],[50,30,28,50,60,70,20,32,54,45])