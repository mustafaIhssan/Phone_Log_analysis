import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
from math import pi,sqrt,sin,cos,atan2

# TODO add date_format defult list 
# TODO add bus['dayofyear'] = pd.DatetimeIndex(bus.time).dayofyear // 
def import_xls_with_all_pages(file_name):
	"""
	import xls files including all the sheets and reset the index.
	:param   file_name: the name and the path from the root for the xls file.
	:return  records:	return pandas dataframe with the data from xls file
	"""
	
	xl = pd.ExcelFile(file_name)

	records = pd.DataFrame()

	for sheet in xl.sheet_names:
		data    = xl.parse(sheet)
		records = records.append(data)
		print((sheet))

	return records.reset_index(drop=True) 

def str_datetime_to_unix(records, old_column, new_column, date_format="%m/%d/%Y %H:%M:%S"):
	"""
	convert string datatime to unix datetime format
	:param records: Be verbose (give additional messages).
	"""
	# convert and replpace datetime to unix time
	# this is for string => datetime => unix
	to_Unix  = lambda x: int(time.mktime(datetime.strptime(x, date_format).timetuple()))
	records[new_column] = records[old_column].apply(to_Unix)
	return records

def str_datetime_to_datetime(records, old_column, new_column, date_format="%m/%d/%Y %H:%M:%S"):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	# convert and replpace string datetime to datetime datatype
	# this is for string => datetime
	"""
	
	str2datetime  = lambda x: datetime.strptime(x, date_format)
	records[new_column] = records[old_column].apply(str2datetime)
	return records

def datetime_to_unix(records, old_column, new_column):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	# convert and replpace datetime to unix time
	# this is for datetime => unix
	to_Unix  = lambda x: int(time.mktime(x.timetuple()))
	records[new_column] = records[old_column].apply(to_Unix)
	return records

def datetime_to_weekdays(records, old_column, new_column):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	# convert and replpace datetime to unix time
	# this is for datetime => weekdays
	to_weekdays  = lambda x : calendar.day_name[x.weekday()]
	records[new_column] = records[old_column].apply(to_weekdays)
	return records

def datetime_to_date(records, old_column, new_column):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	# convert and replpace datetime to unix time
	# this is for datetime => date
	to_date  = lambda x : x.strftime('%Y-%m-%d')
	records[new_column] = records[old_column].apply(to_date)
	return records

def datetime_to_time(records, old_column, new_column):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	# convert and replpace datetime to unix time
	# this is for datetime => time
	to_date  = lambda x : x.strftime('%H:%M:%S')
	records[new_column] = records[old_column].apply(to_date)
	return records


def datetime_to_time_in_sec(records, old_column, new_column):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	# First Recored and Last Record 
	to_sec = lambda x: (x.hour * 60 * 60 + x.minute * 60 + x.second)
	records[new_column] = records[old_column].apply(to_sec)

def IsInRadius(circle_x,circle_y,point_x,point_y,radius):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	delta_x = point_x - circle_x
	delta_y = point_y - circle_y
	delta   = delta_x**2 + delta_y**2
	return delta < radius**2

def distant(circle_x,circle_y,point_x,point_y):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	delta_x = point_x - circle_x
	delta_y = point_y - circle_y
	delta   = delta_x**2 + delta_y**2
	return delta

def  point_on_a_circle_circumference_from_angle(x,y,cx,cy,r,a):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	# output is point in cirlce gevin the ceenter and the angle  
	x = cx + r * cos(a)
	y = cy + r * sin(a)
	return [x,y]

def threshold_distance_from_point(records,records_lat_column_name,records_lng_column_name,stops_df,stop_lat_column_name,stop_lng_column_name,threshold = 20):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	'''
	records input should be :

				stop_1	stop_2	stop_3	...
		index 	-----	------	-----	...
				....	....	....	...
	
	stops_df input should be :

				Latitude  Longitude
		stop 	00.00000  00.00000
				....	  ...

	'''
	for idx, col in enumerate(records.columns):
		records[col] = distant(stops_df.stop_lon.stop_lat_column_name[idx],
								stops_df.stop_lat_column_name.iloc[idx],
								records.Longitude,records.Latitude) * 1000000
		records[col] = records[col].apply( lambda x : x if x < threshold  else threshold )
		records[col] = records[col] * -1 + threshold 

	return records

def get_highest_point_from_thresholded_discreetly_data(records,records_datetime,bus_id, bus):
	"""
	Do some things.
	:param verbose: Be verbose (give additional messages).
	"""
	sch = pd.DataFrame(columns=['bus_id','station_id','time'])

	for bus_no in records[bus_id].unique():
		print( bus_no)

		
		highest = 0
		lower_index = 0
		for inx, col in enumerate(bus.columns):
			print( col)
			if inx+1 == len(bus.columns):
				continue
			for index in range(len(bus.index.values)):
				if index+1 == len(bus.index.values):
					break
				a = bus[col].iloc[index]
				b = bus[col].iloc[index+1]
				if a == 0 and b > 0:
					#print( "in)", a
					www = 0
				else:
					if  a > 0 and b == 0 :
						highest = 0
						sch.set_value(len(sch),['bus_id','station_id','time'],[bus_no,col,bus_a[records_datetime].iloc[lower_index]])
					else:
						if highest < a and a > 0:
							highest = a
							lower_index = index
	return sch

def haversine(lat1,long1,lat2,long2):
    lat1  = float(lat1)
    long1 = float(long1)
    lat2  = float(lat2)
    long2 = float(long2)

    degree_to_rad = float(pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = 6367 * c
    # mi = 3956 * c

    return km