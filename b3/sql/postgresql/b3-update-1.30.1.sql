CREATE TABLE IF NOT EXISTS plugin_nader_hof (
  map_name VARCHAR(255) NOT NULL DEFAULT '',
  player_id INTEGER NOT NULL DEFAULT '0',
  score VARCHAR(10) NOT NULL DEFAULT '0',
  CONSTRAINT map_name UNIQUE (map_name)
);

CREATE TABLE IF NOT EXISTS plugin_knifer_hof (
  map_name VARCHAR(255) NOT NULL DEFAULT '',
  player_id INTEGER NOT NULL DEFAULT '0',
  score VARCHAR(10) NOT NULL DEFAULT '0',
  CONSTRAINT map_name UNIQUE (map_name)
);
