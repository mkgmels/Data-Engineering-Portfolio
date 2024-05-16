select genre,
	album_name
from spotify_datawarehouse
where album_name is not null
	and album_name <> ''
	and genre is not null
	and genre <> ''
limit 10;
