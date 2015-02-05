drop table if exists entries;

create table entries (
  id integer primary key autoincrement,
  priority integer not null,
  category text not null,
  descirption text not null
);