drop table if exists tasks;

create table tasks (
  id integer primary key autoincrement,
  priority integer not null,
  category text not null,
  description text not null
);