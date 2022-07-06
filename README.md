Библиотека invest

Задачи:
 ✓ Разобрать библиотеку на rest api v1 от daxartio 
 ◦ Построить иерархию библиотеки
 ◦ Тз

Иерархия файлов/каталогов 

Tests

Invest
Schemas.py 
Составляем enums (перечисления)
Для сервиса аккаунтов:
 1. AccountType
 1. AccountStatus
 2. AccessLevel
 3. SecurityTraidingStatus
Для сервиса инструментов
 1. CouponType
 2. InstrumentType
 3. InstrumentStatus
 4. ShareType
 5. AssetType
 6. StructuredProductType
 7. EditFavouritesActionType
 8. RealExchange 
 9. SecurityTraidingStatus 
Для сервиса торговых поручений
 1. OrderDirection
 2. OrderType
 3. OrderExecutionReportStatus
 4. SecurityTraidingStatus
Для сервиса операций 
 1. OperationState
 2. OperationType
 3. SecurityTraidingStatus
Для сервиса стоп-заявок 
 1. StopOrderDirection
 2. StopOrderExpirationType
 3. StopOrderType
 4. SecurityTraidingStatus

Models.py (Сообщения, ответы методов, для того что бы их распарсить)

Для сервиса аккаунтов - https://tinkoff.github.io/investAPI/users/#_2

Для сервиса 


APIs.py
Clients.py
Utils.py
Constants.py
Exceptions.py
