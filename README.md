# diplom_3
# проект автоматизации тестирования ui продукта stellarburgers
использовались фреймворки pytest, selenium
в папке tests все тесты
для запуска тестов необходима установка зависимостей pip install -r requirements.txt, а также Google Chrome, Firefox
тесты запускаются в терминале из корневой директории проекта  ./diplom_3 командами pytest 
либо для более подробного вывода pytest -v
Для запуска тестов с отчетом allure используется команда pytest tests --alluredir=allure_results
Далее для формирования отчета в формате веб-страницы команда allure serve allure_results 

какие проверки покрывают тесты:
-Переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
-Ввод почты и клик по кнопке «Восстановить»,
-Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его,
-Переход по клику на «Личный кабинет»,
-Переход в раздел «История заказов»,
-Выход из аккаунта,
-Переход по клику на «Конструктор»,
-Переход по клику на «Лента заказов»,
-Если кликнуть на ингредиент, появится всплывающее окно с деталями,
-Всплывающее окно закрывается кликом по крестику,
-При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
-Залогиненный пользователь может оформить заказ,
-Если кликнуть на заказ, откроется всплывающее окно с деталями,
-Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
-При создании нового заказа счётчик Выполнено за всё время увеличивается,
-При создании нового заказа счётчик Выполнено за сегодня увеличивается,
-После оформления заказа его номер появляется в разделе В работе.