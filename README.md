Перед Вами два файла:
  - mainBot - основной (пользовательский) функционал бота. Реализованы команды, позволяющие делать запросы из БД. 
  - randomFunc - скрипт запускается 1 раз, только для того чтобы записать в последний столбец БД пары.

Изначально графа pair в БД есть Null (NONE в python). После выполнения скрипта randomFunc - в данное поле записывается случайное, неповторяющееся id пользователя из БД.

Работает. Проверено на живых юзерах. Есть баги. В доработке.

Табличка БД выглядит следующим образом - ![image](https://github.com/Rige214/secretSantaTelegramBot/assets/40599394/a9493624-e6e7-4880-873e-3c8c6609a31f)

*UPD 01-09-2024:* 

Доработан скрипт randomFunc . Исключена возможность, когда пользователь является парой сам себе.  Также проект находится в доработке. 
