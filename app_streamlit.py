from word_template.lib import mkw
import streamlit as st
import pandas as pd


prefijo = ['Don', 'Doña']
mes = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
dia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
ciudad = ['Puerto Varas', 'Puerto Montt', 'Santiago']
ano = [2021, 2022,2023,2024,2025,2026,2027]

#category_code = st.selectbox("Category", categories, index=0)

st.subheader('Información Empresa y Dueño')
nombre_empresa = st.text_input('Nombre de la empresa')
empresa_nombre_corto = st.text_input('Nombre corto empresa')
ciudad_empresa = st.selectbox("Ciudad Empresa", ciudad, index=0)
calle_empresa = st.text_input('Calle y numero de la empresa')
rut_empresa = st.text_input('Rut de la empresa')
nombre_dueno = st.text_input('Nombre de Representante Legal')
rut_dueno = st.text_input('Rut del Representante Legal')


st.subheader('Información personal del Trabajador')
prefijo_nombre_empleado = st.selectbox("Don/Doña", prefijo, index=0)
nombre_empleado = st.text_input('Nombre trabajador')
rut_empleado = st.text_input('Rut trabajador')
nacimiento_empleado = st.text_input('Fecha de nacimiento trabajador (DD de MM de AAAA)')
direccion_empleado = st.text_input('Direccion trabajador')
comuna_empleado = st.text_input('Comuna del trabajador')


st.subheader('Información trabajador para contrato')
cargo_empleado = st.text_input('Cargo de trabajador')
sueldo = st.text_input('Sueldo a asignar (con puntos y sin signo $)')
bono_movilizacion = st.text_input('Cantidad de bono movilización (con puntos)')
isapre = st.text_input('Isapre del trabajador')
afp = st.text_input('AFP del trabajador')

st.subheader('Fechas de inicio y termino de contrato')
dia_comienzo_contrato = st.selectbox("Dia COMIENZO contrato", dia, index=0)
mes_comienzo_contrato = st.selectbox("Mes COMIENZO contrato", mes, index=0)
ano_comienzo_contrato = st.selectbox("Año COMIENZO contrato", ano, index=0)

dia_termino_contrato = st.selectbox("Dia TERMINO contrato", dia, index=0)
mes_termino_contrato = st.selectbox("Mes TERMINO contrato", mes, index=0)
ano_termino_contrato = st.selectbox("Año TERMINO contrato", ano, index=0)



st.write(mkw(nombre_empresa, ciudad_empresa, calle_empresa ,rut_empresa, nombre_dueno, rut_dueno, prefijo_nombre_empleado, nombre_empleado,
        rut_empleado, nacimiento_empleado, direccion_empleado, comuna_empleado, cargo_empleado, empresa_nombre_corto, sueldo, bono_movilizacion,
        isapre, afp, dia_termino_contrato,  mes_termino_contrato, ano_termino_contrato, dia_comienzo_contrato, mes_comienzo_contrato,ano_comienzo_contrato
         ))


df = pd.DataFrame({'x': list(range(10)), 'y': list(range(10))})
st.write(df)

if st.button('Download Dataframe as CSV'):
    tmp_download_link = mkw(nombre_empresa, ciudad_empresa, calle_empresa ,rut_empresa, nombre_dueno, rut_dueno, prefijo_nombre_empleado, nombre_empleado,
        rut_empleado, nacimiento_empleado, direccion_empleado, comuna_empleado, cargo_empleado, empresa_nombre_corto, sueldo, bono_movilizacion,
        isapre, afp, dia_termino_contrato,  mes_termino_contrato, ano_termino_contrato, dia_comienzo_contrato, mes_comienzo_contrato,ano_comienzo_contrato
         )
    st.markdown(tmp_download_link, unsafe_allow_html=True)

s = st.text_input('Enter text here')
st.write(s)

