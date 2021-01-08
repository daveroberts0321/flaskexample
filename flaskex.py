
from flask import *
import pandas as pd 
from matplotlib import pyplot as plt


app = Flask(__name__)


# Sales Data and Variables 
salesdata= pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vR5VNWSdsP5Auc6xfCuMzZM3fyDdpw_6oZ9jGUEYQXvkCNYPenWZSkTkPbfOLt0kni0s9nJ53_Da-Xu/pub?output=csv')
x= salesdata.DATE
a= salesdata.BLK15
b= salesdata.FDE15
c= salesdata.OD15
d= salesdata.RIF15
e= salesdata.STL15
f= salesdata.CLR15
g= salesdata.OTH15
#308 Variables
h,i,j,k,l,m = salesdata.BLK308, salesdata.FDE308, salesdata.OD308, salesdata.RIF308,salesdata.STL308, salesdata.OTH308
#TAC9 Variables
n,o,p,q,r = salesdata.BLK9, salesdata.FDE9, salesdata.RIF9, salesdata.STL9, salesdata.OTH9
#80% variables 
s,t,u,v,w,jig,drill = salesdata.BLK80, salesdata.FDE80, salesdata.RIF80, salesdata.STL80, salesdata.OTH80, salesdata.JIGS, salesdata.DRILLBIT
#Consumables 
brass= sum(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w)
sernum= sum(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r)
tac9arm= sum(n+o+p+q+r)
tac9ej= sum(n+o+p+q+r)
tac9but= sum(n+o+p+q+r)
kit15= salesdata.KIT15
buffer15= salesdata.BUFF
kit308= salesdata.KIT308
buffer308= salesdata.BUFF308
buffer9= salesdata.BUFF9
#Pistol Buffers
Pistolbuf15=salesdata.PB15
PistolShk15=salesdata.PS15
PistolSb15=salesdata.SB15
Pistolbuf9=salesdata.PB9
PistolBub9=salesdata.b9
PistolShk9=salesdata.PS9
PistolSb9=salesdata.SB9
#Pistol Buffer 30 day

#Data VisualizationVariables Total Sales
ar15total= sum(a+b+c+d+e+f+g)
ar308total= sum(h+i+j+k+l+m)
tac9total= sum(n+o+p+q+r)
blank80total= sum(s+t+u+v+w)

#running 30 day averages 
a30,b30,c30,d30,e30,f30,g30 = salesdata.BLK15[-30:], salesdata.FDE15[-30:], salesdata.OD15[-30:], salesdata.RIF15[-30:], salesdata.STL15[-30:], salesdata.CLR15[-30:], salesdata.OTH15[-30:]
h30,i30,j30,k30,l30,m30 = salesdata.BLK308[-30:], salesdata.FDE308[-30:], salesdata.OD308[-30:], salesdata.RIF308[-30:],salesdata.STL308[-30:], salesdata.OTH308[-30:]
n30,o30,p30,q30,r30 = salesdata.BLK9[-30:], salesdata.FDE9[-30:], salesdata.RIF9[-30:], salesdata.STL9[-30:], salesdata.OTH9[-30:]
s30,t30,u30,v30,w30,jig30,drill30 = salesdata.BLK80[-30:], salesdata.FDE80[-30:], salesdata.RIF80[-30:], salesdata.STL80[-30:], salesdata.OTH80[-30:], salesdata.JIGS[-30:], salesdata.DRILLBIT[-30:]
#30 day average visualization
ar15total30= sum(a30+b30+c30+d30+e30+f30+g30)
ar308total30= sum(h30+i30+j30+k30+l30+m30)
tac9total30= sum(n30+o30+p30+q30+r30)
blank80total30= sum(s30+t30+u30+v30+w30)

#30 day consumables 
sernum30 = sum(a30+b30+c30+d30+e30+f30+g30)
brass30= sum(a30+b30+c30+d30+e30+f30+g30+h30+i30+j30+k30+l30+m30+n30+o30+p30+q30+r30)
tac9arm30= sum(n30+o30+p30+q30+r30)
tac9ej30= sum(n30+o30+p30+q30+r30)
tac9but30= sum(n30+o30+p30+q30+r30)
kit1530= salesdata.KIT15[-30:]
buffer1530= salesdata.BUFF[-30:]
kit30830= salesdata.KIT308[-30:]
buffer30830= salesdata.BUFF308[-30:]
buffer930= salesdata.BUFF9[-30:]

@app.route('/')
def index():
    ''' this is showing the code for entering and storing form data, th first and last data would 
    go on the next page in the string  '''
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('index.html')

@app.route('/ar15')
def ar15():
    ''' averages and sales data grabbed from https://docs.google.com/spreadsheets/d/1tXv5PI9SP7KGI8zfbSH-xTlRO6zcG-__7RFTWbhfz-Y/edit#gid=0
    '''
    # total average sales
    averageblk15= sum(a30)
    averagefde15= sum(b30)
    averageod15= sum(c30)
    averagerif15= sum(d30)
    averagestl15= sum(e30)
    averageclr15=sum(f30)
    averageoth15= sum(g30)
    # Average 30 days 
    monaverageblk15= round(sum(a30)/len(a30)) 
    monaveragefde15= round(sum(b30)/len(b30))
    monaverageod15= round(sum(c30)/len(c30))
    monaveragerif15= round(sum(d30)/len(d30))
    monaveragestl15= round(sum(e30)/len(e30))
    monaverageclr15=round(sum(f30)/len(f30))
    monaverageoth15= round(sum(g30)/len(g30))
        
    return render_template('ar15.html', averageblk15=averageblk15, averagefde15=averagefde15, averageod15=averageod15,averagerif15=averagerif15,averagestl15=averagestl15,
                              averageclr15=averageclr15,averageoth15=averageoth15, monaverageblk15=monaverageblk15,monaveragefde15=monaveragefde15,monaverageod15=monaverageod15
                              ,monaveragerif15=monaveragerif15,monaveragestl15=monaveragestl15,monaverageclr15=monaverageclr15, monaverageoth15=monaverageoth15)
@app.route('/ar308')
def ar308():
  
  averageblk308= sum(h30) 
  averagefde308= sum(i30)
  averageod308= sum(j30)
  averagerif308= sum(k30)
  averagestl308= sum(l30)
  averageoth308= sum(m30)
  monaverageblk308= round(sum(h30)/len(h30)) 
  monaveragefde308= round(sum(i30)/len(i30))
  monaverageod308= round(sum(j30)/len(j30))
  monaveragerif308= round(sum(k30)/len(k30))
  monaveragestl308= round(sum(l30)/len(l30))
  monaverageoth308=round(sum(m30)/len(m30))

  return render_template('ar308.html',averageblk308=averageblk308, averagefde308=averagefde308, averageod308=averageod308, averagerif308=averagerif308
                           ,averagestl308=averagestl308,averageoth308=averageoth308, monaverageblk308=monaverageblk308,monaveragefde308=monaveragefde308
                           , monaverageod308=monaverageod308, monaveragerif308=monaveragerif308, monaveragestl308=monaveragestl308,monaverageoth308=monaverageoth308 )
@app.route('/tac9')
def tac9():

  #n30,o30,p30,q30,r30 = salesdata.BLK9[-30:], salesdata.FDE9[-30:], salesdata.RIF9[-30:], salesdata.STL9[-30:], salesdata.OTH9[-30:]
  
  avblk9= sum(n30) 
  avfde9= sum(o30)
  avrif9= sum(p30)
  avstl9= sum(q30)
  avoth9= sum(r30)
  monavblk9= round(sum(n30)/len(n30)) 
  monavfde9= round(sum(o30)/len(o30))
  monavrif9= round(sum(p30)/len(p30))
  monavstl9= round(sum(q30)/len(q30))
  monavoth9= round(sum(r30)/len(r30))
  return render_template('tac9.html',avblk9=avblk9, avfde9=avfde9, avrif9=avrif9, avstl9=avstl9,avoth9=avoth9
                           ,monavblk9=monavblk9, monavfde9=monavfde9, monavrif9=monavrif9, monavstl9=monavstl9, monavoth9=monavoth9)
        
@app.route('/blank80')
#s,t,u,v,w,jig,drill = salesdata.BLK80, salesdata.FDE80, salesdata.RIF80, salesdata.STL80, salesdata.OTH80, salesdata.JIGS, salesdata.DRILLBIT
def blank80():
  avblk80= sum(s30) 
  avfde80= sum(t30)
  avrif80= sum(j30)
  avstl80= sum(k30)
  avoth80= sum(l30)
  avjig80= sum(jig30)
  avdrill80=sum(drill30)
  monavblk80= round(sum(s30)/len(s30)) 
  monavfde80= round(sum(i30)/len(i30))
  monavrif80= round(sum(j30)/len(j30))
  monavstl80= round(sum(k30)/len(k30))
  monavoth80= round(sum(l30)/len(l30))
  monavjig80=round(sum(jig30)/len(jig30))
  monavdrill80= round(sum(drill30)/len(drill30))
  return render_template('blank80.html',avblk80=avblk80, avfde80=avfde80, avrif80=avrif80, avstl80=avstl80, avoth80=avoth80, avjig80=avjig80, avdrill80=avdrill80,
                          monavblk80=monavblk80, monavfde80=monavfde80, monavrif80=monavrif80, monavstl80=monavstl80, monavjig80=monavjig80,monavdrill80=monavdrill80)


@app.route('/consumables')
def consumables():
  
  sernum30 = sum(a30+b30+c30+d30+e30+f30+g30)
  brass30= sum(a30+b30+c30+d30+e30+f30+g30+h30+i30+j30+k30+l30+m30+n30+o30+p30+q30+r30)
  tac9arm30= sum(n30+o30+p30+q30+r30)
  tac9ej30= sum(n30+o30+p30+q30+r30)
  tac9but30= sum(n30+o30+p30+q30+r30)
  kit1530= sum(salesdata.KIT15[-30:])
  buffer1530= sum(salesdata.BUFF[-30:])
  kit30830= sum(salesdata.KIT308[-30:])
  buffer30830= sum(salesdata.BUFF308[-30:])
  buffer930= sum(salesdata.BUFF9[-30:])
  


  return render_template('consumables.html',sernum30=sernum30, brass30=brass30, tac9arm30=tac9arm30, tac9ej30=tac9ej30, tac9but30=tac9but30,
                          kit1530=kit1530, buffer1530=buffer1530, kit30830=kit30830, buffer30830=buffer30830, buffer930=buffer930)

@app.route('/salessplits')
def salessplits():
  #variables
  ar15sales= a30+b30+c30+d30+e30+f30+g30
  ar308sales= h30+i30+j30+k30+l30+m30
  tac9sales= n30+o30+p30+q30+r30
  blank80= s30+t30+u30+v30+w30
  totalsales= ar15sales+ ar308sales+tac9sales+blank80
  perar15=round(sum(ar15sales)*100/sum(totalsales))
  perar308=round(sum(ar308sales)*100/sum(totalsales))
  pertac9=round(sum(tac9sales)*100/sum(totalsales))
  per80=round(sum(blank80)*100/sum(totalsales))

  return render_template('salessplits.html', ar15sales=sum(ar15sales), ar308sales=sum(ar308sales), tac9sales=sum(tac9sales), blank80=sum(blank80), 
                          totalsales=sum(totalsales), perar15=perar15, perar308=perar308, pertac9=pertac9, per80=per80)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 