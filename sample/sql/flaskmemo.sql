-- DBの基本操作

-- テーブルの作成
create table memo(
  id integer primary key autoincrement,
  title text not null,
  body text not null
);

-- 誤って作成したテーブルの削除
drop table memo;

-- データの挿入
insert into memo (title,body) values(
  "First Message", "Hello World"
);

insert into memo (title,body) values(
  "Second Message", "Hello takehiro1111"
);

-- 挿入したデータの確認
select * from memo;

select * from memo where id=2;

-- データの更新
update memo set title="update_test",body="updateのデータです。" where id=2;

-- データの削除
delete from memo where id=2;

-- トランザクションの管理(begin-rollback)
BEGIN;

delete from memo;
select * from memo;

ROLLBACK;

-- トランザクションの管理(begin-commit)
BEGIN;

select * from memo;
delete from memo where id=3;
select * from memo;

COMMIT;
