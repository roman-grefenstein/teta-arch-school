# Контекст решения
<!-- Окружение системы (роли, участники, внешние системы) и связи системы с ним. Диаграмма контекста C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783261
-->

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()


Person(administrator, "Администратор", "Пользователь ИС управляющий конференцией")
Person(reviewer, "Рецензент", "Пользователь ИС проводящией рецензии докладов")
Person(support, "Эксплуатация", "Инженеры эксплуатации обеспечивающие поддержку ИС")

Person_Ext(author, "Докладчик", "Участник конференции, выступающий c докладом по определенной теме")
Person_Ext(user, "Слушатель", "Участник конференции, который смотрит трансляцию или запись")

System(is, "Информационная система HelloConf", "Система для проведения видеоконференций")

System_Ext(video, "Платформа видеотрансляции", "Платформа для записи и трансляции видеопотока")
System_Ext(notification, "Платформа нотификаций", "Платформа для оповещения пользователей по e-mail/sms")

Rel(author, is, "Uses")
Rel(administrator, is, "Uses")
Rel(reviewer, is, "Uses")
Rel(support, is, "Uses")
Rel(user, is, "Uses")
Rel(is, video, "Use")
Rel(is, notification, "Use")
@enduml
```
