@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Iniciando servidor Flask (app.py)
python C:\Users\pedro\Desktop\skill_localizador_material-main\app.py

timeout /t 3 >nul

