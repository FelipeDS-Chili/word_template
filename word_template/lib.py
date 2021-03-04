# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for word_template Project
"""
from docxtpl import DocxTemplate
from os.path import split
import pandas as pd
import datetime
import locale
import time


time.strftime("%A %d %B %Y").upper()

def mkw(nombre_empresa, ciudad_empresa, calle_empresa ,rut_empresa, nombre_dueno, rut_dueno, prefijo_nombre_empleado, terminacion ,nombre_empleado,
        rut_empleado, nacimiento_empleado, direccion_empleado, comuna_empleado, cargo_empleado, empresa_nombre_corto, sueldo, bono_movilizacion,
        isapre, afp, dia_termino_contrato,  mes_termino_contrato, ano_termino_contrato, dia_comienzo_contrato, mes_comienzo_contrato,ano_comienzo_contrato
         ):

    tpl = DocxTemplate('template.docx')

    context = {
    'nombre_empresa': nombre_empresa.upper(),
    'ciudad_empresa': ciudad_empresa,
    'fecha_actual': traducir(time.strftime("%A %d de %B del %Y").upper()),

    'rut_empresa': rut_empresa,
    'nombre_dueno': nombre_dueno.upper(),
    'rut_dueno': rut_dueno,
    'calle_empresa': calle_empresa,
    'prefijo_nombre_empleado': prefijo_nombre_empleado,
    'terminacion': terminacion,
    'nombre_empleado': nombre_empleado.upper(),
    'rut_empleado': rut_empleado,
    'nacimiento_empleado': nacimiento_empleado,
    'direccion_empleado': direccion_empleado,
    'comuna_empleado': comuna_empleado,
    'cargo_empleado': cargo_empleado.upper(),
    'empresa_nombre_corto': empresa_nombre_corto,
    'sueldo': sueldo,
    'bono_movilizacion': bono_movilizacion,
    'isapre': isapre.upper(),
    'afp': afp.upper(),
    'dia_termino_contrato':dia_termino_contrato,
    'mes_termino_contrato':mes_termino_contrato,
    'ano_termino_contrato':ano_termino_contrato,
    'dia_comienzo_contrato':dia_comienzo_contrato,
    'mes_comienzo_contrato':mes_comienzo_contrato,
    'ano_comienzo_contrato':ano_comienzo_contrato,
    'ciudad_contrato':ciudad_empresa
    }

    tpl.render(context)
    tpl.save('Contrato.docx')

    return DocxTemplate('Contrato.docx')



def traducir (fecha):

    mes_en = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

    mes_esp = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]

    dia_en =["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    dia_esp = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]

    for idx, mes in enumerate(mes_en):
        fecha = fecha.replace(mes, mes_esp[idx])

    for idx, dia in enumerate(dia_en):
        fecha = fecha.replace(dia, dia_esp[idx])

    return fecha

if __name__ == '__main__':

    mkw('hola')
