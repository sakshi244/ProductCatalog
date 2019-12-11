create database product_catalog

use product_catalog;

create table if not exists `product_details`
(
   `product_id` int not null auto_increment,
   `product_name` varchar(1000) not null,
   `product_brand` varchar(1000) not null,

    primary key(`product_id`)
) ENGINE=InnoDB;

create table if not exists `product_categories`
(
   `id` int not null auto_increment,
   `product_id` int not null,
   `category` varchar(1000) not null,

    foreign key (product_id) REFERENCES product_details(product_id),
    primary key(`id`)
) ENGINE=InnoDB;

create table if not exists `product_images`
(
   `id` int not null auto_increment,
   `product_id` int not null,
   `image_url` varchar(1000) not null,

    foreign key (product_id) REFERENCES product_details(product_id),
    primary key(`id`)
) ENGINE=InnoDB;