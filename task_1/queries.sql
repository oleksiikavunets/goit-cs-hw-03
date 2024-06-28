--Отримати всі завдання певного користувача
select * from tasks where user_id = 1

--Вибрати завдання за певним статусом
select * from tasks where status_id = (select id from status where name = 'new')

--Оновити статус конкретного завдання
update tasks set status_id = 2 where id = 12

--Отримати список користувачів, які не мають жодного завдання
select * from users where id not in (select distinct user_id from tasks)

--Додати нове завдання для конкретного користувача
insert into tasks (title, description, status_id, user_id) values ('Foo Bar', 'Biz Buzz', 1, 1)

--Отримати всі завдання, які ще не завершено
select * from tasks where status_id in (select id from status where name <> 'completed')

--Видалити конкретне завдання
delete from tasks where id = 13

--Знайти користувачів з певною електронною поштою
select * from users where email like '%net%'

--Оновити ім'я користувача
update users set fullname = 'Van Damm' where id = 7

--Отримати кількість завдань для кожного статусу
select s.name, count(*) as count from status s join tasks t on s.id = t.status_id group by s."name"

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
select * from tasks t join users u on t.user_id = u.id where u.email like '%@example%'

--Отримати список завдань, що не мають опису.
select * from tasks where description is null

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
select u.fullname, t.title from users u join tasks t on u.id = t.user_id join status s on s.id = t.status_id where s."name" = 'in progress'

--Отримати користувачів та кількість їхніх завдань.
select u.fullname, count(*) from users u left join tasks t on u.id = t.user_id group by u.fullname order by count desc