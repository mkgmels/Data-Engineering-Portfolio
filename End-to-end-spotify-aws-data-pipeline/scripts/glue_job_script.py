import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node artists
artists_node1715764849894 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://mkg-spotify-data/spotify_staging/artists.csv"], "recurse": True}, transformation_ctx="artists_node1715764849894")

# Script generated for node albums
albums_node1715764851052 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://mkg-spotify-data/spotify_staging/albums.csv"], "recurse": True}, transformation_ctx="albums_node1715764851052")

# Script generated for node tracks
tracks_node1715764848426 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://mkg-spotify-data/spotify_staging/tracks.csv"], "recurse": True}, transformation_ctx="tracks_node1715764848426")

# Script generated for node artists_albums_join
artists_node1715764849894DF = artists_node1715764849894.toDF()
albums_node1715764851052DF = albums_node1715764851052.toDF()
artists_albums_join_node1715766247891 = DynamicFrame.fromDF(artists_node1715764849894DF.join(albums_node1715764851052DF, (artists_node1715764849894DF['id'] == albums_node1715764851052DF['artist_id']), "outer"), glueContext, "artists_albums_join_node1715766247891")

# Script generated for node tracks_join
tracks_node1715764848426DF = tracks_node1715764848426.toDF()
artists_albums_join_node1715766247891DF = artists_albums_join_node1715766247891.toDF()
tracks_join_node1715766595557 = DynamicFrame.fromDF(tracks_node1715764848426DF.join(artists_albums_join_node1715766247891DF, (tracks_node1715764848426DF['track_id'] == artists_albums_join_node1715766247891DF['track_id']), "outer"), glueContext, "tracks_join_node1715766595557")

# Script generated for node Drop Fields
DropFields_node1715766761293 = DropFields.apply(frame=tracks_join_node1715766595557, paths=["album_id", "artist_id"], transformation_ctx="DropFields_node1715766761293")

# Script generated for node Destination
Destination_node1715766860139 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1715766761293, connection_type="s3", format="glueparquet", connection_options={"path": "s3://mkg-spotify-data/spotify_datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1715766860139")

job.commit()
