create database epidemic ;

use epidemic;

create table t_epidemic(
    id int primary key auto_increment ,

    region varchar(50) comment '区域',

    addCon int comment '每日新增确诊病例',

    addDon int comment '每日新增疑似病例',

    epidemic_time date comment '录入时间'
);