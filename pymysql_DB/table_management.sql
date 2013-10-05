create database if not exists ios_compare_db;
-- DEFAULT CHARACTER SET utf8
-- DEFAULT COLLATE utf8_general_ci;

create user 'bia_user'@'localhost' identified by 'biabiabia';

grant all privileges on ios_compare_db.* to 'bia_user'@'localhost';

use ios_compare_db;

create table if not exists ios_four_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists ios_five_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists ios_six_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists ios_seven_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone3gs_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone4_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone4s_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone5_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone5s_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone5s_only_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

create table if not exists iphone5c_only_tweets
(
	usr_id varchar(255),
	usr_name varchar(255),
	usr_url varchar(255),
	tw_content varchar(255),
	tw_url varchar(255) primary key,
	tw_time datetime
);

describe ios_four_tweets;

select * from iphone3gs_tweets;
select count(*) from iphone3gs_tweets;

show tables;

select * from iphone4_tweets;
select count(*) from iphone4_tweets;

select * from iphone4s_tweets;
select count(*) from iphone4s_tweets;

select * from iphone5_tweets;
select count(*) from iphone5_tweets;

select * from iphone5s_tweets;
select count(*) from iphone5s_tweets;

select * from iphone5s_only_tweets;
select count(*) from iphone5s_only_tweets;

select * from iphone5c_only_tweets;
select count(*) from iphone5c_only_tweets;

select tw_url, tw_content, tw_time from ios_four_tweets order by tw_time DESC;
select * from ios_four_tweets order by tw_time;
select * from ios_five_tweets;
select * from ios_six_tweets;
select * from ios_seven_tweets;

select count(*) from ios_four_tweets;
select count(*) from ios_five_tweets;
select count(*) from ios_six_tweets;
select count(*) from ios_seven_tweets;

commit;
-- insert ignore into ios_four_tweets values( 'ratkat\ ', 'Nick\ Robinson', 'http\:\/\/twitter\.com\/ratkat\ ', '\@timsalmon\ \ felt\ like\ I\ was\ using\ new\ phone\ briefly\ when\ I\ installed\ iOS4\,\ some\ nice\ features\,\ l\ like\ the\ unified\ inbox\ \&\ rotation\ lock\ best', 'http\:\/\/twitter\.com\/Ratkat\/status\/16106746744', '2010-06-13 17:04:00');
/*
drop table if exists ios_four_tweets;
drop table if exists ios_five_tweets;
drop table if exists ios_six_tweets;
drop table if exists ios_seven_tweets;
drop user 'bia_user'@'localhost';
drop database if exists ios_compare_db;
*/