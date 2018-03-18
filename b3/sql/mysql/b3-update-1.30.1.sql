CREATE TABLE IF NOT EXISTS `plugin_nader_hof` (
  `map_name` varchar(255) NOT NULL default '',
  `player_id` smallint(5) unsigned NOT NULL default '0',
  `score` varchar(10) NOT NULL default '0',
  PRIMARY KEY  (`map_name`),
  UNIQUE KEY `map_name` (`map_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `plugin_knifer_hof` (
  `map_name` varchar(255) NOT NULL default '',
  `player_id` smallint(5) unsigned NOT NULL default '0',
  `score` varchar(10) NOT NULL default '0',
  PRIMARY KEY  (`map_name`),
  UNIQUE KEY `map_name` (`map_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
