create schema amnesiainterview;

create table amnesiainterview.interview (
    content_id      integer     not null,
    last_name       smalltext   not null,
    first_name      smalltext   not null,
    position        smalltext,
    affiliation     smalltext,
    picture_id      integer     not null,
    body            text        not null,
    twitter         url,
    linkedin        url,
    facebook        url,
    instagram       url,
    researchgate    url,

    constraint pk_interview
        primary key(content_id),

    constraint fk_content
        foreign key(content_id) references content(id),

    constraint fk_file
        foreign key(picture_id) references data(content_id)
);

insert into content_type(name, icons)
values('interview', '{"fa": "fa-microphone-alt"}');
