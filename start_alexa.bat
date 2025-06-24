@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Iniciando servidor Flask (app.py) em nova janela...
start cmd /k python app.py

timeout /t 3 >nul

echo Iniciando ngrok na porta 5000...
start cmd /k ngrok http 5000

echo Tudo pronto!
