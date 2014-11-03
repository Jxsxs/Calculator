# -*- coding: utf-8 -*-

from lettuce import *
from Calculator import Calculator

@step(u'Tengo dos numeros (\d+)')
def tengo_dos_numeros(step,a,b):
    world.a = int(a)
    world.b = int(b)

@step(u'Elijo suma, resta, division o multi')
def elijo_suma_resta_division_o_multi(step):
	cal = Calculator()
	world.result = cal.suma(world.a,world.b)

@step(u'Calculo el resultado (\d+)')
def calculo_el_resultado(step,esperado):
    assert world.result == esperado

