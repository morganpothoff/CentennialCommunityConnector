

/***********************************************************************************************************************
*                                                                                                                      *
*   created by:                                                                                                        *
*   on 2021.11.13                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION:                                                                                                       *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


-- State Farm created
CREATE TABLE `Counselors`
(
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`description` TEXT NOT NULL DEFAULT '',
	`education` TEXT NOT NULL DEFAULT '',
	`name` VARCHAR(128) NOT NULL,
	`practice` TEXT NOT NULL,
	`specialities` TEXT NOT NULL,
	`title` VARCHAR(64) NOT NULL,
);


-- Not directly viewed by the front end
CREATE TABLE `EventCounselors`
(
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`Counselors.id` BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY `Counselors.id` REFERENCES `Counselors`(`id`),
	`Events.id` BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY `Events.id` REFERENCES `Events`(`id`)
);


-- Dropdown
CREATE TABLE `EventsType`
(
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`description` TEXT NOT NULL DEFAULT '',
	`label` VARCHAR(32),
	`requirements` TEXT NOT NULL DEFAULT ''
);


-- State Farm created
CREATE TABLE `Events`
(
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`reason` TEXT NOT NULL,
	`EventsType.id` BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY `EventsType.id` REFERENCES `EventsType`(`id`),
	`address` VARCHAR(128),
	`city` VARCHAR(64),
	`state` CHAR(2) NOT NULL,
	`zip` CHAR(5) NOT NULL  -- postal zip code
);


-- User created
CREATE TABLE `Request`
(
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`email` VARCHAR(64) NOT NULL,
	`reason` TEXT NOT NULL,
	`time` DATETIME NOT NULL,
	`EventsType.id` BIGINT UNSIGNED NOT NULL,
	FOREIGN KEY `EventsType.id` REFERENCES `EventsType`(`id`),
	`is_virtual` BOOLEAN NOT NULL DEFAULT FALSE
	`zip` CHAR(5) NOT NULL  -- postal zip code
);