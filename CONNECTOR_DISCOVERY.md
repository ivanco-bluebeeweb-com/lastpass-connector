# LastPass Connector — Connector Discovery

**Official Documentation:** https://lastpass.com  
**Base URL:** https://lastpass.com/enterpriseapi.php  
**Auth Model:** Enterprise API Key + CID  

## Основные сущности вендора
- пользователи (/batchusers), общие папки (/sharedfolders), отчеты о событиях (/eventreport)

## Лимиты и особенности API
- Соблюдение Rate Limits вендора, обработка HTTP 429 с экспоненциальным backoff.
- Валидация входных данных по Pydantic-схемам вендора до отправки запроса.
- Тестовая точка проверки подключения: `POST /enterpriseapi.php (cmd: getuserdata)`.
