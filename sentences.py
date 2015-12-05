#coding: utf-8

import rulesets
import words
import spelling_mode

reload(rulesets)
reload(words)
reload(spelling_mode)

from rulesets import *
from words import *

# Biologie in Theorie und Praxis.
def sentence1():
  return b(c=C_NOUN|C_BOS)+i()+o()+l()+o()+g()+ie()+space()+i()+n()+space()+th(c=C_NOUN)+e()+o()+r()+ie()+space()+u()+n()+d()+space()+p(c=C_NOUN)+r()+a()+x()+i()+s()+fs()+para() 
       
# Physik ist schwer. Chemie ist dumm.
def sentence2():
  return ph(c=C_NOUN|C_BOS)+y()+s()+i()+k()+space()+i()+s()+t()+space()+sch()+w()+e()+r()+fs()+para()+ch(c=C_NOUN|C_BOS, m=CH_GREEK)+e()+m()+ie()+space()+i()+s()+t()+space()+d()+u()+mm()+fs()+para()

# Die kleine Nuss mit großer Masse liegt auf der Straße.
def sentence3(): 
  return d(c=C_BOS)+ie()+space()+k()+l()+ei()+n()+e()+space()+n(c=C_NOUN)+u()+sz(m=EOW)+space()+m()+i()+t()+space()+g()+r()+o()+sz()+e()+r()+space()+m(c=C_NOUN)+a()+ss()+e()+space()+l()+ie()+g()+t()+space()+au()+f()+space()+d()+e()+r()+space()+st(c=C_NOUN)+r()+a()+sz()+e()+fs()

# Viele Häuser sind Beute von kecken Dachsen.
def sentence4():
  return viel(c=C_BOS)+e()+space()+h(c=C_NOUN)+aumlu()+s()+e()+r()+space()+sind()+space()+b(c=C_NOUN)+eu()+t()+e()+space()+von()+space()+k()+e()+ck()+e()+n()+space()+d(c=C_NOUN)+a()+ch(m=CH_CK)+s()+e()+n()+fs()
  
# Der Cellist spielt für ein paar Cent im Casino bei 5 Grad Celcius.
def sentence5():
  return der(c=C_BOS)+space()+c(c=C_NOUN, m=C_TSCH)+e()+ll()+i()+s()+t()+space()+sp()+ie()+l()+t()+space()+fuer()+space()+ein()+space()+p()+aa()+r()+space()+c(c=C_NOUN, m=C_S)+e()+n()+t()+space()+i()+m()+space()+c(c=C_NOUN)+a()+s()+i()+n()+o()+space()+bei()+space()+"5"+space()+g(c=C_NOUN)+r()+a()+d(m=VOICELESS)+space()+c(c=C_NOUN, m=C_Z)+e()+l()+s()+i()+u()+s()+fs()

# Casimir und Wendy sind zwei durchschnittliche Deutsche.
def sentence001():
  return casimir(c=C_BOS)+space()+und()+space()+wendy()+space()+sind()+space()+z()+w()+ei()+space()+d()+u()+r()+ch()+sch()+n()+i()+tt()+l()+i()+ch()+e()+space()+d(c=C_NOUN)+eu()+t()+sch()+e()+fs()
  
# Sie haben viel gemeinsam, unterscheiden sich aber durch sehr stark abweichende Sichten auf die deutsche Rechtschreibung.  
def sentence002():
  return sie(c=C_BOS)+space()+h()+a()+b()+e()+n()+space()+v()+ie()+l()+space()+g()+e()+m()+ei()+n()+s()+a()+m()+comma_sc()+space()+u()+n()+t()+e()+r()+sch()+ei()+d()+e()+n()+space()+s()+i()+ch()+space()+a()+b()+e()+r()+space()+d()+u()+r()+ch()+space()+s()+eh()+r()+space()+st()+a()+r()+k()+space()+a()+b()+w()+ei()+ch()+e()+n()+d()+e()+space()+s(c=C_NOUN)+i()+ch()+t()+e()+n()+space()+au()+f()+space()+die()+space()+d()+eu()+t()+sch()+e()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+fs()

# Casimir ist eher konservativ und möchte am liebsten den Status Quo wiederherstellen, wie er vor der Rechtschreibreform im Jahre 1996 gültig war.
def sentence003():
  return casimir(c=C_BOS)+space()+ist()+space()+e()+h()+e()+r()+space()+k()+o()+n()+s()+e()+r()+v(m=VOICEFULL)+a()+t()+i()+v()+space()+und()+space()+m()+ouml()+ch()+t()+e()+space()+a()+m()+space()+l()+ie()+b()+s()+t()+e()+n()+space()+d()+e()+n()+space()+s(c=C_NOUN)+t()+a()+t()+u()+s()+space()+qu(c=C_NOUN)+o()+space()+w()+ie()+d()+e()+r()+h()+e()+r()+s()+t()+e()+ll()+e()+n()+comma_sc()+space()+w()+ie()+space()+e()+r()+space()+v()+o()+r()+space()+der()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+r()+e()+f()+o()+r()+m()+space()+i()+m()+space()+j(c=C_NOUN)+ah()+r()+e()+space()+"1996"+space()+g()+uuml()+l()+t()+i()+g()+space()+w()+a()+r()+fs()
   
# Wendy ist eher fortschrittlich und überlegt ständig, wie man die Rechtschreibung verbessern und vereinfachen kann. 

def sentence004():
  return wendy(c=C_BOS)+space()+ist()+space()+e()+h()+e()+r()+space()+f()+o()+r()+t()+sch()+r()+i()+tt()+l()+i()+ch()+space()+und()+space()+uuml()+b()+e()+r()+l()+e()+g()+t()+space()+st()+auml()+n()+d()+i()+g()+comma_sc()+space()+wie()+space()+man()+space()+die()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+v()+e()+r()+b()+e()+ss()+e()+r()+n()+space()+und()+space()+v()+e()+r()+ei()+n()+f()+a()+ch()+e()+n()+space()+k()+a()+nn()+fs()
  
  
# Diese unterschiedlichen Sichtweisen führen ständig zu Diskussionen und Streitereien.
def sentence005():
  return d(c=C_BOS)+ie()+s()+e()+space()+u()+n()+t()+e()+r()+sch()+ie()+d()+l()+i()+ch()+e()+n()+space()+s(c=C_NOUN)+i()+ch()+t()+w()+ei()+s()+e()+n()+space()+f()+uuml()+h()+r()+e()+n()+space()+st()+auml()+n()+d()+i()+g()+space()+z()+u()+space()+d(c=C_NOUN)+i()+s()+k()+u()+ss()+i()+o()+n()+e()+n()+space()+und()+space()+st(c=C_NOUN)+r()+ei()+t()+e()+r()+ei()+e()+n()+fs() 
     
# Der grundlegende Unterschied ist ganz einfach: Casimir hat in seiner Jugend die damals aktuelle Rechtschreibung kennengelernt und hat sich an sie gewöhnt.
def sentence006():
  return der(c=C_BOS)+space()+g()+r()+u()+n()+d()+l()+e()+g()+e()+n()+d()+e()+space()+u(c=C_NOUN)+n()+t()+e()+r()+sch()+ie()+d(m=VOICELESS)+space()+ist()+space()+g()+a()+n()+z()+space()+ei()+n()+f()+a()+ch()+colon()+space()+casimir(c=C_BOS_AC)+space()+hat()+space()+i()+n()+space()+s()+ei()+n()+e()+r()+space()+j(c=C_NOUN)+u()+g()+end()+space()+die()+space()+d()+a()+m()+a()+l()+s()+space()+a()+k()+t()+u()+e()+ll()+e()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+k()+e()+nn()+e()+n()+g()+e()+l()+e()+r()+n()+t()+space()+und()+space()+hat()+space()+sich()+space()+a()+n()+space()+sie()+space()+g()+e()+w()+oumlh()+n()+t()+fs()
  
# Er hat die Regeln verinnerlicht und denkt heute nicht mehr über ihre Sinnhaftigkeit nach.
def sentence007():
  return e(c=C_BOS)+r()+space()+hat()+space()+die()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+v()+e()+r()+i()+nn()+e()+r()+l()+i()+ch()+t()+space()+und()+space()+d()+e()+n()+k()+t()+space()+h()+eu()+t()+e()+space()+n()+i()+ch()+t()+space()+m()+eh()+r()+space()+uuml()+b()+e()+r()+space()+ih()+r()+e()+space()+s(c=C_NOUN)+i()+nn()+h()+a()+f()+t()+i()+g()+k()+ei()+t()+space()+n()+a()+ch()+fs()
   
# Zwar sind viele der Regeln durchaus logisch und nachvollziehbar.
def sentence008():
  return z(c=C_BOS)+w()+a()+r()+space()+sind()+space()+v()+ie()+l()+e()+space()+der()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+d()+u()+r()+ch()+au()+s()+space()+l()+o()+g()+i()+sch()+space()+und()+space()+n()+a()+ch()+v()+o()+ll()+z()+ie()+h(m=MUTE)+b()+a()+r()+fs()
    
# Es gibt jedoch Gegenbeispiele, die schon aus damaliger Sicht unlogisch waren.
def sentence009():
  return e(c=C_BOS)+s()+space()+g()+i()+b()+t()+space()+j()+e()+d()+o()+ch()+space()+g(c=C_NOUN)+e()+g()+e()+n()+b()+ei()+sp()+ie()+l()+e()+comma_sc()+space()+die()+space()+sch()+o()+n()+space()+aus()+space()+d()+a()+m()+a()+l()+i()+g()+e()+r()+space()+s(c=C_NOUN)+i()+ch()+t()+space()+u()+n()+l()+o()+g()+i()+sch()+space()+w()+a()+r()+e()+n()+fs()
  
# Besonders störend sind dabei die Fälle, bei denen sich die Aussprache von Worten nicht aus dem Schriftbild ableiten lässt.
def sentence010():
  return b(c=C_BOS)+e()+s()+o()+n()+d()+e()+r()+s()+space()+st()+ouml()+r()+end()+space()+sind()+space()+d()+a()+b()+ei()+space()+die()+space()+f(c=C_NOUN)+auml()+ll()+e()+comma_sc()+space()+bei()+space()+d()+e()+n()+e()+n()+space()+sich()+space()+die()+space()+a(c=C_NOUN)+u()+s()+sp()+r()+a()+ch()+e()+space()+von()+space()+w(c=C_NOUN)+o()+r()+t()+e()+n()+space()+n()+i()+ch()+t()+space()+aus()+space()+dem()+space()+sch(c=C_NOUN)+r()+i()+f()+t()+b()+i()+l()+d(m=VOICELESS)+space()+a()+b()+l()+ei()+t()+e()+n()+space()+l()+auml()+ss()+t()+fs()
  
#  Casimir möchte dennoch diesen althergebrachten Regelsatz erhalten und damit das Schriftbild, das ihm aus fast der gesamten heute verfügbaren Literatur vertraut ist.
def sentence011():
  return casimir(c=C_BOS)+space()+m()+ouml()+ch()+t()+e()+space()+d()+e()+nn()+o()+ch()+space()+d()+ie()+s()+e()+n()+space()+a()+l()+t()+h()+e()+r()+g()+e()+b()+r()+a()+ch()+t()+e()+n()+space()+r(c=C_NOUN)+e()+g()+e()+l()+s()+a()+t()+z()+space()+e()+r()+h()+a()+l()+t()+e()+n()+space()+und()+space()+d()+a()+m()+i()+t()+space()+das()+space()+sch(c=C_NOUN)+r()+i()+f()+t()+b()+i()+l()+d()+comma_sc()+space()+das()+space()+ih()+m()+space()+aus()+space()+f()+a()+s()+t()+space()+der()+space()+g()+e()+s()+a()+m()+t()+e()+n()+space()+h()+eu()+t()+e()+space()+v()+e()+r()+f()+uuml()+g()+b()+a()+r()+e()+n()+space()+l(c=C_NOUN)+i()+t()+e()+r()+a()+t()+u()+r()+space()+v()+e()+r()+t()+r()+a()+u()+t()+space()+ist()+fs()
  
# Wendy hat einen anderen Ansatz. 
def sentence012():
  return wendy(c=C_BOS)+space()+h()+a()+t()+space()+ein()+e()+n()+space()+a()+n()+d()+e()+r()+e()+n()+space()+a(c=C_NOUN)+n()+s()+a()+t()+z()+fs() 
  
# Sie möchte, dass die Rechtschreibung in erster Linie dem Lesenden und Schreibenden hilft, einen Text möglichst einfach zu lesen bzw. zu erstellen. 
def sentence013():
  return sie(c=C_BOS)+space()+m()+ouml()+ch()+t()+e()+comma_sc()+space()+dass()+space()+die()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+i()+n()+space()+e()+r()+s()+t()+e()+r()+space()+l(c=C_NOUN)+i()+n()+i()+e()+space()+dem()+space()+l(c=C_NOUN)+e()+s()+e()+n()+d()+e()+n()+space()+und()+space()+sch(c=C_NOUN)+r()+ei()+b()+e()+n()+d()+e()+n()+space()+h()+i()+l()+f()+t()+comma_sc()+space()+ein()+e()+n()+space()+t(c=C_NOUN)+e()+x()+t()+space()+m()+ouml()+g()+l()+i()+ch()+s()+t()+space()+ei()+n()+f()+a()+ch()+space()+z()+u()+space()+l()+e()+s()+e()+n()+space()+b()+z()+w()+dot_abbr()+space()+z()+u()+space()+e()+r()+st()+e()+ll()+e()+n()+fs() 
  
# Einfach bedeutet dabei mit möglichst einfachen, nachvollziehbaren Regeln. 
#def sentence014():
#  return Einfach bedeutet dabei mit möglichst einfachen, nachvollziehbaren Regeln. 
  
# Auch möchte sie die Anzahl der Regeln so weit wie möglich reduzieren. 
#def sentence015():
#  return Auch möchte sie die Anzahl der Regeln so weit wie möglich reduzieren. 
  
# Die Überarbeitung des Regelsatzes hätte als offensichtlich die zum Teil drastische Änderung des Schriftbildes zur Folge. 
#def sentence016():
#  return Die Überarbeitung des Regelsatzes hätte als offensichtlich die zum Teil drastische Änderung des Schriftbildes zur Folge. 
  
# Kein Satz würde mehr so aussehen wie vorher. 
#def sentence017():
#  return Kein Satz würde mehr so aussehen wie vorher. 
  
# Alle Werke der Literatur müssten angepasst werden. 
#def sentence018():
#  return Alle Werke der Literatur müssten angepasst werden. 
  
# Alle Menschen müssten umlernen. 
#def sentence019():
#  return Alle Menschen müssten umlernen. 
  
# Andererseits könnten sich Kinder schneller das Lesen und Schreiben aneignen, weil sie weniger Zeit mit dem Lernen überflüssiger und inkonsistenter Regeln verschwenden würden. 
#def sentence020():
#  return Andererseits könnten sich Kinder schneller das Lesen und Schreiben aneignen, weil sie weniger Zeit mit dem Lernen überflüssiger und inkonsistenter Regeln verschwenden würden. 
    
# Auch Nichtmuttersprachler würden davon profitieren.  
#def sentence021():
#  return Auch Nichtmuttersprachler würden davon profitieren.  
    
def test():
  rulesets.set_default_mode(rulesets.spelling_mode())
  print sentence001() + space()+ sentence002() + space() + sentence003() + space() + sentence004() + space() + sentence005() + space() + sentence006() + space() + sentence007() + space() + sentence008() + space() + sentence009() + space() + sentence010() + space() + sentence011() + space() + sentence012() + space() + sentence013() +space() + sentence4() + space() + sentence5() 
  
if __name__ == '__main__':
  test()

