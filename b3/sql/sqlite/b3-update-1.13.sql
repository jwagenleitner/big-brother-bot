-- SQL code to update default B3 database tables to B3 version 1.13 --
-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS `plugin_nader_hof` (
  `map_name` VARCHAR(255) NOT NULL DEFAULT '',
  `player_id` INTEGER NOT NULL DEFAULT '0',
  `score` VARCHAR(10) NOT NULL DEFAULT '0'
);

CREATE TABLE IF NOT EXISTS `plugin_knifer_hof` (
  `map_name` VARCHAR(255) NOT NULL DEFAULT '',
  `player_id` INTEGER NOT NULL DEFAULT '0',
  `score` VARCHAR(10) NOT NULL DEFAULT '0'
);
