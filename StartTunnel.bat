@echo off
title LocalTunnel Reconexão Automática
set PORT=5000
set SUBDOMAIN=ativarestoque3
set RETRY=5

:RECONNECT
cls
echo Iniciando tunnel em https://%SUBDOMAIN%.loca.lt...
lt --port %PORT% --subdomain %SUBDOMAIN%

echo.
echo A conexão caiu ou foi encerrada.
echo Tentando reconectar em %RETRY% segundos...
timeout /t %RETRY% /nobreak >nul
goto RECONNECT
