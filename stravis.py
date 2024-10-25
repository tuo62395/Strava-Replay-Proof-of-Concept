#strava vizualizer
import gpxpy
import gpxpy.gpx
import matplotlib.pyplot as plt
import tilemapbase
tilemapbase.start_logging()
tilemapbase.init(create=True)

#use open street map
t = tilemapbase.tiles.build_OSM()

gpx_file = open('file.gpx', 'r')

#createa matplotlib figure
#plt.figure(figsize=(10,8))
#ax = plt.gca()
#ax.set_aspect('equal')

gpx = gpxpy.parse(gpx_file)

point_index = -1
for track in gpx.tracks:
    
    for segment in track.segments:
        
        for point in segment.points:
            point_index += 1
            if point_index % 100 == 0:
                #plot a riding point
                
                degree_range = 0.003
                extent = tilemapbase.Extent.from_lonlat(point.longitude - degree_range, point.longitude + degree_range, 
                                                        point.latitude - degree_range, point.latitude + degree_range)
                extent = extent.to_aspect(1.0)
                extent.project
                
                fig, ax = plt.subplots(figsize=(8,8), dpi=100)
                ax.xaxis.set_visible(False)
                ax.yaxis.set_visible(False)
    

                plotter = tilemapbase.Plotter(extent, t, width=600)
                plotter.plot(ax, t)

                x, y = tilemapbase.project(point.longitude, point.latitude)
                ax.scatter(x,y, marker=".", color="black", linewidth=20)
                plt.pause(0.001)

                

plt.show()
            
                
            



