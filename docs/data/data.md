# Модель предметной области
<!-- Логическая модель, содержащая бизнес-сущности предметной области, атрибуты и связи между ними. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375782602

Используется диаграмма классов UML. Документация: https://plantuml.com/class-diagram 
-->

```plantuml
@startuml
' Логическая модель данных в варианте UML Class Diagram (альтернатива ER-диаграмме).

namespace HelloConf {
    class Conference
    {
        id : int
        name : string
        link : string
        state : ConferenceState
        dateStart : datetime
        dateFinish : datetime
        createdAt : datetime
        updatedAt : datetime
    }

    class User
    {
        id : string        
        name : string
        login : string
        role : Role
        createdAt : datetime
        updatedAt : datetime
    }

    class ReportAuthor
    {
        id : string
        name : string
        phone : string
        email : string
        createdAt : datetime
        updatedAt : datetime
    }

    class Report
    {
        id : string
        autor : ReportAuthor
        name : string
        text : string
        state : ReportState
        user : User
        file : string
        link : string
        createdAt : datetime
        updatedAt : datetime
    }

    class Schedule
    {
        id : string
        name : string
        text : text        
        report : Report
        dateStart : datetime
        dateFinish : datetime
        createdAt : datetime
        updatedAt : datetime
    }

    class Feedback
    {
        id : string
        name : string
        email : string
        text : string
        createdAt : datetime
        updatedAt : datetime
    }

    enum ConferenceState
    {
        init
        planning
        online
        finished
    }

    enum ReportState
    {
        init        
        reviewing
        rejected
        reviewed
        confirmed        
    }

    enum Role
    {
        administrator
        reviewer
    }

    Conference -- ConferenceState
    Conference *-- "0..*" Schedule    
    Report -- User
    ReportAuthor *-- "1..*" Report
    Report -- ReportState    
    Schedule -- Report
    Report *-- "0..*" Feedback
    Schedule -- User
    User -- Role
}

@enduml
```
