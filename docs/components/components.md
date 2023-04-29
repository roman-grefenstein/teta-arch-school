# Компонентная архитектура
<!-- Состав и взаимосвязи компонентов системы между собой и внешними системами с указанием протоколов, ключевые технологии, используемые для реализации компонентов.
Диаграмма контейнеров C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783368
-->
## Контейнерная диаграмма


```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="microservice")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")
AddElementTag("fileStorage", $shape=RoundedBoxShape(),$bgColor="lightSkyBlue")

Person(administrator, "Администратор", "Пользователь ИС управляющий конференцией")
Person(reviewer, "Рецензент", "Пользователь ИС проводящий рецензии докладов")

Person_Ext(author, "Докладчик", "Участник конференции, выступающий c докладом по определенной теме")
Person_Ext(user, "Слушатель", "Участник конференции, который смотрит трансляцию или запись")


System_Boundary(is, "Информационная система HelloConf") {

   Container(fe_web, "Клиентское веб-приложение", "html, JavaScript, Angular", "Сайт конференции")

   Container(fe_admin, "Административный интерфейс", "html, JavaScript, Angular", "Админка")

   Container_Boundary(conference_context, "Конференции") {
      Container(conferences_service, "Сервис для управления конференциями", "Golang", "Сервис управления продуктовым предложением", $tags = "microService")
      Container(users_service, "Сервис для управления пользователями административного интерфейса", "Golang", "Сервис управления пользователями админки", $tags = "microService")
      ContainerDb(conferences_db, "Конференции", "PostgreSQL", "Хранение данных по конференции", $tags = "storage")
      ContainerDb(users_db, "Пользователи", "PostgreSQL", "Хранение пользователей административного интерфейса", $tags = "storage")
   }

   Container_Boundary(report_context, "Доклады") {
      Container(authors_service, "Сервис для управления авторами докладов", "Golang", "Сервис управления авторами", $tags = "microService")
      Container(reports_service, "Сервис для управления докладами", "Golang", "Сервис управления докладами", $tags = "microService")
      Container(feedback_service, "Сервис для управления отзывами", "Golang", "Сервис управления отзывами", $tags = "microService")

      ContainerDb(authors_db, "Докладчики", "PostgreSQL", "Хранение информации по докладчикам", $tags = "storage")
      ContainerDb(reports_db, "Доклады", "PostgreSQL", "Хранение данных по докладам", $tags = "storage")
      ContainerDb(feedback_db, "Отзывы", "PostgreSQL", "Хранение отзывов", $tags = "storage")

      Container(storage_reports, "Файлы докладов", "WebDAV", "Файловое хранилище для докладов", $tags = "fileStorage")
   }
}

System_Ext(video_ext_service, "Платформа видеотрансляции", "Платформа для записи и трансляции видеопотока")
System_Ext(notification_ext_service, "Платформа нотификаций", "Платформа для оповещения пользователей по e-mail/sms")


Rel(user, fe_web, "Просмотр конференции", "HTTPS")
Rel(author, fe_web, "Загрузка контактных данных и докладов", "HTTPS")

Rel(conferences_service, conferences_db, "Хранение данных по конференциям", "SQL")
Rel(conferences_service, reports_service, "Расписание конференции", "HTTPS")
Rel(conferences_service, notification_ext_service, "Отправка нотификаций", "SMTP,HTTPS")

Rel(reports_service, reports_db, "Хранение данных по докладам", "SQL")
Rel(reports_service, storage_reports, "Хранение файлов докладов", "HTTPS")

Rel(administrator, fe_admin, "Заведение пользователей, назначение ревьюверов, составление расписания", "HTTPS")
Rel(reviewer, fe_admin, "Работа с докладами автора", "HTTPS")

Rel(fe_admin, conferences_service, "Работа с докладами автора", "HTTPS")
Rel(fe_admin, users_service, "Работа с докладами автора", "HTTPS")

Rel(fe_web, feedback_service, "Сохранение отзывов", "HTTPS")
Rel(fe_web, video_ext_service, "Трансляция конференции", "HTTPS")
Rel(fe_web, authors_service, "Сохранение данных автора", "HTTPS")
Rel(fe_web, reports_service, "Сохранение доклада", "HTTPS")

Rel(users_service, users_db, "Хранение данных пользователей административного интерфейса", "SQL")
Rel(authors_service, authors_db, "Хранение данных по докладчикам", "SQL")
Rel(feedback_service, feedback_db, "Хранение данных по обратной связки", "SQL")


SHOW_LEGEND()
@enduml
```


## Список компонентов
| Компонент             | Роль/назначение                  |
|:----------------------|:---------------------------------|
| Клиентское веб-приложение | Сайт для проведения онлайн конференция, архивом прошедших конференций и возможностью подать заявку на доклад |
| Административный интерфейс | Интерфейс для работы администраторов конференций и ревьюверов докладов для формирования расписания конференций |
| Сервис для управления конференциями | Микросервис для управления конференциями |
| Сервис для управления пользователями административного интерфейса | Микросервис для управления пользователями админки и управлению ролями |
| Сервис для управления авторами докладов | Микросервис для управления авторами докладов |
| Сервис для управления докладами | Микросервис для управлениями докладами |
| Сервис для управления отзывами | Микросервис для управлениями докладами |
| Конференции | База даннах для хранения информации по конференциям  |
| Пользователи | База даннах для хранения пользователей административного интерфейса |
| Докладчики | База даннах для хранения докладчиков |
| Доклады | База даннах для хранения докладов |
| Отзывы | База даннах для хранения отзывов |
| Файлы докладов | Файловое хранилище для файлов докладов |