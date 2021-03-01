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

def mkw(nombre_empresa, ciudad_empresa, calle_empresa ,rut_empresa, nombre_dueno, rut_dueno, prefijo_nombre_empleado, nombre_empleado,
        rut_empleado, nacimiento_empleado, direccion_empleado, comuna_empleado, cargo_empleado, empresa_nombre_corto, sueldo, bono_movilizacion,
        isapre, afp, dia_termino_contrato,  mes_termino_contrato, ano_termino_contrato, dia_comienzo_contrato, mes_comienzo_contrato,ano_comienzo_contrato
         ):
    tpl = DocxTemplate('template.docx')
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    context = {
    'nombre_empresa': nombre_empresa,
    'ciudad_empresa': ciudad_empresa,
    'fecha_actual': time.strftime("%A %d de %B del %Y").upper(),

    'rut_empresa': rut_empresa,
    'nombre_dueno': nombre_dueno,
    'rut_dueno': rut_dueno,
    'calle_empresa': calle_empresa,
    'prefijo_nombre_empleado': prefijo_nombre_empleado,
    'nombre_empleado': nombre_empleado,
    'rut_empleado': rut_empleado,
    'nacimiento_empleado': nacimiento_empleado,
    'direccion_empleado': direccion_empleado,
    'comuna_empleado': comuna_empleado,
    'cargo_empleado': cargo_empleado,
    'empresa_nombre_corto': empresa_nombre_corto,
    'sueldo': sueldo,
    'bono_movilizacion': bono_movilizacion,
    'isapre': isapre,
    'afp': afp,
    'dia_termino_contrato':dia_termino_contrato,
    'mes_termino_contrato':mes_termino_contrato,
    'ano_termino_contrato':ano_termino_contrato,
    'dia_comienzo_contrato':dia_comienzo_contrato,
    'mes_comienzo_contrato':mes_comienzo_contrato,
    'ano_comienzo_contrato':ano_comienzo_contrato,
    'ciudad_contrato':ciudad_empresa
    }

    tpl.render(context)

    return tpl.save('Contrato.docx')


if __name__ == '__main__':

    mkw('hola')
