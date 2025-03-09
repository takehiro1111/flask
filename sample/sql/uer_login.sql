create table user(
  unum integer primary key AUTOINCREMENT,
  userid text not null unique,
  password text not null
);


-- テーブルの存在確認
 select * from sqlite_master;
