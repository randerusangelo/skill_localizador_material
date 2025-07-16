@echo off
chcp 65001 >nul
title LocalTunnel - Reconexão Automática

REM Configurações
set PORT=5000
set SUBDOMAIN=ativarestoque3
set RETRY=5
set LOGFILE=tunnel_log.txt

REM Gera timestamp para o log
:RECONNECT
for /f "tokens=1-3 delims=/" %%a in ('date /t') do set DATA=%%c-%%b-%%a
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set HORA=%%a-%%b

echo. >> %LOGFILE%
echo [%DATA% %HORA%] Tentando iniciar tunnel em https://%SUBDOMAIN%.loca.lt >> %LOGFILE%
echo [%DATA% %HORA%] Tentando iniciar tunnel em https://%SUBDOMAIN%.loca.lt 
echo ============================================= 
echo Iniciando tunnel em https://%SUBDOMAIN%.loca.lt
echo =============================================

REM Executa LocalTunnel com log
cmd /c "lt --port %PORT% --subdomain %SUBDOMAIN%" >> %LOGFILE% 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo !!! ERRO OU CONEXÃO ENCERRADA !!!
    echo [%DATA% %HORA%] Erro detectado. Código de erro: %ERRORLEVEL% >> %LOGFILE%
)

echo.
echo ---------------------------------------------
echo A conexão caiu ou foi encerrada.
echo Tentando reconectar em %RETRY% segundos...
echo ---------------------------------------------
echo [%DATA% %HORA%] Reconectando em %RETRY% segundos... >> %LOGFILE%
timeout /t %RETRY% /nobreak >nul
goto RECONNECT
