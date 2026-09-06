# LastPass Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** Enterprise API Key + CID
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `POST /enterpriseapi.php (cmd: getuserdata)`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
