# Hawaii-hw
homework of 11-Advanced-Data-Storage-and-Retrieval

## Usage
### Analysis part
1. run `jupyter notebook`
```
$ cd Hawaii-hw
$ jupyter notebook
```
2. the notebook will open automatically, it's composed of following 3 analyses.
    
    * Part1. data_engineering.ipynb
    * Part2. database_engineering.ipynb
    * Part3. climate_analysis.ipynb

### Climate App
1. run `app.py`
```
$ cd Hawaii-hw
$ python3 app.py
```

2. visit [http://localhost/5000](http://localhost/5000) on your browser

#### Climate App endpoints and responses
* `/api/v1.0/preceipitation` returns a json list of preceipitations (prcps) for the last year.
```
[
  {
    "date": "2017-01-01", 
    "prcp": 0.0
  }, 
  {
    "date": "2017-01-01", 
    "prcp": 0.29
  }, 
  {
    "date": "2017-01-01", 
    "prcp": 0.0
  }, 
  {
    "date": "2017-01-01", 
    "prcp": 0.03
  }, 
  {
    "date": "2017-01-01", 
    "prcp": 0.03
  }, 
  {
    "date": "2017-01-02", 
    "prcp": 0.0
  }, 
  {
    "date": "2017-01-02", 
    "prcp": 0.0
  }, 
  {
    "date": "2017-01-02", 
    "prcp": 0.01
  },
  ...
]
```

* `/api/v1.0/stations` return a json list of stations from the dataset.
```
[
  {
    "name": "WAIKIKI 717.2, HI US", 
    "station": "USC00519397"
  }, 
  {
    "name": "KANEOHE 838.1, HI US", 
    "station": "USC00513117"
  }, 
  {
    "name": "KUALOA RANCH HEADQUARTERS 886.9, HI US", 
    "station": "USC00514830"
  }, 
  {
    "name": "PEARL CITY, HI US", 
    "station": "USC00517948"
  }, 
  ...
]
```

* `/api/v1.0/tobs` returns a json list of Temperature Observations (tobs) for the last year
```
[
  {
    "date": "2017-01-01", 
    "tobs": 62
  }, 
  {
    "date": "2017-01-02", 
    "tobs": 66
  }, 
  {
    "date": "2017-01-03", 
    "tobs": 63
  }, 
  {
    "date": "2017-01-04", 
    "tobs": 62
  }, 
  {
    "date": "2017-01-05", 
    "tobs": 63
  }, 
  {
    "date": "2017-01-06", 
    "tobs": 64
  }, 
  ...
 ]
```

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>` return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

```
  {
    "TAVG": 74.54576271186441, 
    "TMAX": 87.0, 
    "TMIN": 58.0
  }
```
  
