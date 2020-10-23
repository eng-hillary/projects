//map showing farms
var H = Highcharts,
    map = H.maps['countries/ug/ug-all'],
    chart;

var json = Highcharts.getJSON('/farm/api/maps/', function (json) {
    var data = [];
    json.forEach(function (p) {
        p.z = p.land_occupied;
        data.push(p);
    })

    select.addEventListener('change', (e) => {
      var district = e.target.value;
      var districtArr = Highcharts.defaultOptions;
      var districtIndex = districtArr.indexOf(district) + 1;
      // var data = [];
    
      for (var j = 0; j < json.data.length; j++) {
        data.push([
          json.data[j][0], +json.data[j][districtIndex]
        ]);
      }
    //console.log(data);
    
      Highcharts.charts.forEach((chart) => {
        chart.series[0].update({
          data: data
        }, false, false, false);
    
        chart.redraw();
      });
    });
    
  chart = Highcharts.mapChart('farm_container', {
    title: {
      text: 'Farmers Locations'
  },
  
  mapNavigation: {
      enabled: true,
      buttonOptions: {
          verticalAlign: 'bottom'
      }
  },
 
  tooltip: {
      pointFormat: 'id: {point.id}<br>' +
          'district: {point.district}<br>' +
          'farmer: {point.farmer}<br>' +
          'farm name: {point.farm_name}<br>' +
          'land occupied: {point.land_occupied}'+ ' acres'

  },

  xAxis: {
      crosshair: {
          zIndex: 5,
          dashStyle: 'dot',
          snap: false,
          color: 'gray'
      }
  },

  yAxis: {
      crosshair: {
          zIndex: 5,
          dashStyle: 'dot',
          snap: false,
          color: 'gray'
      }
  },
  plotOptions:{
      series:{
          point:{
              events:{
                  click: function(event){
                       var url = "/farm/"+ event.point.id +"/view/";
                       window.location.href = url;
                      //alert(event.point.id);
                  }
              }
          }
      }
  },
  series: [{
    name: 'Basemap',
    mapData: map,
    borderColor: '#B0B0B0',
    nullColor: 'rgba(200, 200, 200, 0.2)',
    showInLegend: false
}, {
    name: 'Separators',
    type: 'mapline',
    data: H.geojson(map, 'mapline'),
    color: '#101010',
    enableMouseTracking: false,
    showInLegend: false
}, {
    type: 'mapbubble',
    dataLabels: {
        enabled: true,
        format: '{point.farm_name}'
    },
    name: 'Farms',
    data: data,
    maxSize: '5%',
    color: 'green'
}],
});
});

//map showing resources
 Highcharts.getJSON('/resourcesharing/api/resource/', function (json) {
  var data = [];
  json.forEach(function (p) {
      p.z = p.id;
      data.push(p);
  })
//console.log(data);
 
  chart = Highcharts.mapChart('resource_container', {
      title: {
          text: 'Resource Locations'
      },
      
      mapNavigation: {
          enabled: true,
          buttonOptions: {
              verticalAlign: 'bottom'
          }
      },
     
      tooltip: {
          pointFormat: 'ID: {point.id}<br>' +
          'District: {point.district}<br>' +
          'Owner: {point.owner}<br>' +
          'Resource Status: {point.resource_status}<br>' +
          'Price: {point.price}<br>' + 'shs'
          
      },

      xAxis: {
          crosshair: {
              zIndex: 5,
              dashStyle: 'dot',
              snap: false,
              color: 'gray'
          }
      },

      yAxis: {
          crosshair: {
              zIndex: 5,
              dashStyle: 'dot',
              snap: false,
              color: 'gray'
          }
      },
      plotOptions:{
          series:{
              point:{
                  events:{
                      click: function(event){
                           var url = "/resourcesharing/"+ event.point.id +"/view/";
                           window.location.href = url;
                          //alert(event.point.id);
                      }
                  }
              }
          }
      },
      series: [{
          name: 'Basemap',
          mapData: map,
          borderColor: '#B0B0B0',
          nullColor: 'rgba(200, 200, 200, 0.2)',
          showInLegend: false
      }, {
          name: 'Separators',
          type: 'mapline',
          data: H.geojson(map, 'mapline'),
          color: '#101010',
          enableMouseTracking: false,
          showInLegend: false
      }, {
          type: 'mapbubble',
          dataLabels: {
              enabled: true,
              format: '{point.resource_name}'
          },
          name: 'Resources',
          data: data,
          maxSize: '5%',
          color: 'blue'
      }]
  });
});


// Display custom label with lat/lon next to crosshairs
document.getElementById('resource_container').addEventListener('mousemove', function (e) {
  var position;
  if (chart) {
      if (!chart.lab) {
          chart.lab = chart.renderer.text('', 0, 0)
              .attr({
                  zIndex: 5
              })
              .css({
                  color: '#505050'
              })
              .add();
      }

      e = chart.pointer.normalize(e);
      position = chart.fromPointToLatLon({
          x: chart.xAxis[0].toValue(e.chartX),
          y: chart.yAxis[0].toValue(e.chartY)
      });
      
      chart.lab.attr({
          x: e.chartX + 5,
          y: e.chartY - 22,
          text: 'Lat: ' + position.lat.toFixed(2) + '<br>Lon: ' + position.lon.toFixed(2)
      });
  }
});


document.getElementById('resource_container').addEventListener('mouseout', function () {
  if (chart && chart.lab) {
      chart.lab.destroy();
      chart.lab = null;
  }
});

//map showing services
Highcharts.getJSON('/openmarket/api/serviceregistration/', function (json) {
  var data = [];
  json.forEach(function (p) {
      p.z = p.id;
      data.push(p);
  })

 
  chart = Highcharts.mapChart('service_container', {
      title: {
          text: 'Service Locations'
      },
      
      mapNavigation: {
          enabled: true,
          buttonOptions: {
              verticalAlign: 'bottom'
          }
      },
     
      tooltip: {
          pointFormat: 'id: {point.id}<br>' +
              'Service Name: {point.service_name}<br>' +
              'Service Type: {point.service_type}<br>' +
              'Availability Date: {point.availability_date}<br>' 
    
      },

      xAxis: {
          crosshair: {
              zIndex: 5,
              dashStyle: 'dot',
              snap: false,
              color: 'gray'
          }
      },

      yAxis: {
          crosshair: {
              zIndex: 5,
              dashStyle: 'dot',
              snap: false,
              color: 'gray'
          }
      },
      plotOptions:{
          series:{
              point:{
                  events:{
                      click: function(event){
                           var url = "/openmarket/"+ event.point.id +"/view/";
                           window.location.href = url;
                          //alert(event.point.id);
                      },
                  }
              }
          }
      },
      series: [{
          name: 'Basemap',
          mapData: map,
          borderColor: '#B0B0B0',
          nullColor: 'rgba(200, 200, 200, 0.2)',
          showInLegend: false
      }, {
          name: 'Separators',
          type: 'mapline',
          data: H.geojson(map, 'mapline'),
          color: '#101010',
          enableMouseTracking: false,
          showInLegend: false
      }, {
          type: 'mapbubble',
          dataLabels: {
              enabled: true,
              format: '{point.service_name}'
          },
          name: 'services',
          data: data,
          maxSize: '5%',
          color: 'red'
      }]
  });
});


// Display custom label with lat/lon next to crosshairs
document.getElementById('service_container').addEventListener('mousemove', function (e) {
  var position;
  if (chart) {
      if (!chart.lab) {
          chart.lab = chart.renderer.text('', 0, 0)
              .attr({
                  zIndex: 5
              })
              .css({
                  color: '#505050'
              })
              .add();
      }

      e = chart.pointer.normalize(e);
      position = chart.fromPointToLatLon({
          x: chart.xAxis[0].toValue(e.chartX),
          y: chart.yAxis[0].toValue(e.chartY)
      });
    
      chart.lab.attr({
          x: e.chartX + 5,
          y: e.chartY - 22,
          text: 'Lat: ' + position.lat.toFixed(2) + '<br>Lon: ' + position.lon.toFixed(2)
      });
  }
});


document.getElementById('service_container').addEventListener('mouseout', function () {
  if (chart && chart.lab) {
      chart.lab.destroy();
      chart.lab = null;
  }
});


// Create the chart
Highcharts.chart('piecontainer', {
  chart: {
    type: 'pie'
  },
  title: {
    text: 'Browser market shares. January, 2018'
  },
  subtitle: {
    text: 'Click the slices to view versions. Source: <a href="http://statcounter.com" target="_blank">statcounter.com</a>'
  },

  accessibility: {
    announceNewData: {
      enabled: true
    },
    point: {
      valueSuffix: '%'
    }
  },

  plotOptions: {
    series: {
      dataLabels: {
        enabled: true,
        format: '{point.name}: {point.y:.1f}%'
      }
    }
  },

  tooltip: {
    headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
    pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total farmers<br/>'
  },

  series: [
    {
      name: "Browsers",
      colorByPoint: true,
      data: [
        {
          name: "Western",
          y: 62.74,
          drilldown: "Western"
        },
        {
          name: "Northern",
          y: 10.57,
          drilldown: "Northern"
        },
        {
          name: "Central",
          y: 7.23,
          drilldown: "Central"
        },
        {
          name: "Eastern",
          y: 5.58,
          drilldown: "Eastern"
        },
        // {
        //   name: "Edge",
        //   y: 4.02,
        //   drilldown: "Edge"
        // }
      ]
    }
  ],
  drilldown: {
    series: [
      {
        name: "Eastern Region",
        id: "Eastern Region",
        data: [
          [
            "v65.0",
            0.1
          ],
          [
            "v64.0",
            1.3
          ],
          [
            "v63.0",
            53.02
          ],
          [
            "v62.0",
            1.4
          ],
          [
            "v61.0",
            0.88
          ],
          [
            "v60.0",
            0.56
          ],
          [
            "v59.0",
            0.45
          ],
          [
            "v58.0",
            0.49
          ],
          [
            "v57.0",
            0.32
          ],
          [
            "v56.0",
            0.29
          ],
          [
            "v55.0",
            0.79
          ],
          [
            "v54.0",
            0.18
          ],
          [
            "v51.0",
            0.13
          ],
          [
            "v49.0",
            2.16
          ],
          [
            "v48.0",
            0.13
          ],
          [
            "v47.0",
            0.11
          ],
          [
            "v43.0",
            0.17
          ],
          [
            "v29.0",
            0.26
          ]
        ]
      },
      {
        name: "Western Region",
        id: "Western Region",
        data: [
          [
            "v58.0",
            1.02
          ],
          [
            "v57.0",
            7.36
          ],
          [
            "v56.0",
            0.35
          ],
          [
            "v55.0",
            0.11
          ],
          [
            "v54.0",
            0.1
          ],
          [
            "v52.0",
            0.95
          ],
          [
            "v51.0",
            0.15
          ],
          [
            "v50.0",
            0.1
          ],
          [
            "v48.0",
            0.31
          ],
          [
            "v47.0",
            0.12
          ]
        ]
      },
      {
        name: "Northen Region",
        id: "Northen Region",
        data: [
          [
            "v11.0",
            6.2
          ],
          [
            "v10.0",
            0.29
          ],
          [
            "v9.0",
            0.27
          ],
          [
            "v8.0",
            0.47
          ]
        ]
      },
      {
        name: "Central Region",
        id: "Central Region",
        data: [
          [
            "v11.0",
            6.2
          ],
          [
            "v10.0",
            0.29
          ],
          [
            "v9.0",
            0.27
          ],
          [
            "v8.0",
            0.47
          ]
        ]
      }
    ]
  }
});
 

// Create the chart

Highcharts.getJSON('/farmer/api/farmerprofiles/', function (json) {
  var data = [];
  json.forEach(function (p) {
      p.z = p.region;
      data.push(p);
  })

//console.log(data);



Highcharts.chart('barcontainer', {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Percentage of Farmers in each Region with credit Access'
  },
  subtitle: {
    text: 'Source: <a href="https://en.wikipedia.org/wiki/World_population">Wikipedia.org</a>'
  },
  xAxis: {
    categories: ['Western Region', 'Eastern Region', 'Northern Region', 'Central Region'],
    title: {
      text: null
    }
  },
  yAxis: {
    min: 0,
    title: {
      text: 'Population of Farmers',
      align: 'high'
    },
    labels: {
      overflow: 'justify'
    }
  },
  tooltip: {
    valueSuffix: ' Farmer/s'
  },
  plotOptions: {
    bar: {
      dataLabels: {
        enabled: true
      }
    }
  },
  legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'top',
    x: -40,
    y: 80,
    floating: true,
    borderWidth: 1,
    backgroundColor:
      Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
    shadow: true
  },
  credits: {
    enabled: false
  },
  series: [{
    name: 'Credit Access',
    data: [1, 1, 0, 1]
  }, {
    name: ' No credit access',
    data: [2, 2, 1, 1]
  }]
});
})


/// open weather api//
$(document).ready(function () {
  var options = {
    enableHighAccuracy: true,
    timeout: 10000,
    maximumAge: 0
  };
  
  function success(pos) {
    var crd = pos.coords;
    var wheather_api = "https://api.openweathermap.org/data/2.5/weather?lat="+crd.latitude+"&lon="+crd.longitude+"&appid=b63fe7d4cf27f561ccaed0342922db91";
    var dairy_weather_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+crd.latitude+"&lon="+crd.longitude+"&exclude=hourly,current,minutely,&appid=b63fe7d4cf27f561ccaed0342922db91";
    //console.log(dairy_weather_url);
    // console.log('Your current position is:');
    // console.log(`Latitude : ${crd.latitude}`);
    // console.log(`Longitude: ${crd.longitude}`);
    // console.log(`More or less ${crd.accuracy} meters.`);
    $.ajax({
      url: wheather_api,
      dataType: 'json',
      type:'GET',
      data:{units:'metric'},
      success:function(data){
        
        var weather='';
        $.each(data.weather, function(index,val){
          var icon ="http://openweathermap.org/img/wn/"+val.icon+"@2x.png"
          weather+='<img src='+icon+'><br>'+'<p><h3>'+ data.name+'</b></h3>'+
          data.main.temp +'&deg;C'+'|'+val.main+ ','+
          val.description

        });
        $('#showweather').html(weather);
      }

    });
   
 
  }
  
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }
  
  navigator.geolocation.getCurrentPosition(success, error, options);


  var getFutureDate = function (day) {
    var someDate = new Date();
    var numberOfDaysToAdd = day;
    someDate.setDate(someDate.getDate() + numberOfDaysToAdd); 
  
    var dd = someDate.getDate();
    var mm = someDate.getMonth();
    var y = someDate.getFullYear();
    var d = someDate.getDay();
  
    // convert month number to month name
    var month = new Array();
    month[0] = 'January';
    month[1] = 'February';
    month[2] = 'March';
    month[3] = 'April';
    month[4] = 'May';
    month[5] = 'June';
    month[6] = 'July';
    month[7] = 'August';
    month[8] = 'September';
    month[9] = 'October';
    month[10] = 'November';
    month[11] = 'December';
  
    // convert day number into day name
    var day = new Array();
    day[1] = 'Monday';
    day[2] = 'Tuesday';
    day[3] = 'Wednesday';
    day[4] = 'Thursday'; 
    day[5] = 'Friday';
    day[6] = 'Saturday';
    day[0] = 'Sunday';
  
    var futureMonth = month[mm];
    var futureDay = day[d];
  
    var someFormattedDate = futureDay + ", " + futureMonth + ' '+ dd + ', '+ y;
  
    return someFormattedDate;
  }
  // Function evaluates "clouds" conditions between 1 and 100 and returns image index
  var getClouds = function(clouds) {
    if ( 100 < clouds && clouds < 90 ) {
      // return Cloudy Object
      var condition = {
        cloudNumber: 6,
        cloudText: 'Cloudy'
      };
      return condition;
    } else if ( 89 < clouds && clouds < 60 ) {
      // return Mostly Cloudy
      var condition = {
        cloudNumber: 5,
        cloudText: 'Mostly Cloudy'
      };
      return condition;
    } else if ( 59 < clouds && clouds < 30 ) {
      // return Partly Cloudy
      var condition = {
        cloudNumber: 4,
        cloudText:'Partly Cloudy'
      };
    } else if (29 < clouds && clouds > 20) {
      // return Mostly Sunny
      var condition =  {
        cloudNumber: 3,
        cloudText: 'Mostly Sunny'
      };
      return condition;
    } else if ( 19 > clouds && clouds > 10 ) {
      // return Sunny to Mostly Sunny
      var condition = {
        cloudNumber: 2,
        cloudText: 'Sunny to Mostly Sunny'
      };
      return condition;
    } else {
      // return Sunny
      var condition = {
        cloudNumber: 1,
        cloudText: 'Sunny'
      };
      return condition;
    }
  }
  
  // Function: Handlebar Module / CRPA ("Crapa") (Create, Reference, Pass & Append)
  var getWeather = function(theForecast) {
    // City Label
    $('#results').html(theForecast.city.name);
    // REFERENCE from HTML
    var source = $('#weather-spot').html();
    // compile to Handlebars
    var template = Handlebars.compile(source);
  
    // create loop to get x days worth of data.  "list" is key name.
    for (var i = 1 ; i < theForecast.list.length; i++) {
      // get future dates
      var futureDate = getFutureDate(i);
      var cloudsCondition = getClouds(theForecast.list[i].clouds);
      
      // build weather data object for Handlebars
      var weatherData = {
        now: futureDate,
        average: Math.round(theForecast.list[i].temp.day),
        high: Math.round(theForecast.list[i].temp.max),
        low: Math.round(theForecast.list[i].temp.min),
        morning: Math.round(theForecast.list[i].temp.morn),
        nighttime: Math.round(theForecast.list[i].temp.night),
        cloudInfo: cloudsCondition.cloudNumber,
        cloudInfoText: cloudsCondition.cloudText,
        weatherText:theForecast.list[i].weather[0].description
      }
      
      // PASS weather data object to template via the variable "fullText"
      var fullText = template(weatherData);
  
      // APPEND fullText to the div.container
      $('.container').append(fullText);
    }
  };
  
  // Function: Call api.openweathermap.com
  var APICall = function(theCity) {
    // get API url
    var weatherUrl = "http://api.openweathermap.org/data/2.5/forecast/daily?q=" + theCity;
    // get API key
    var apiKey = "b0b34e0501286ae903bab8dde901b6ae";
    // get "unit" as imperial
    var unitType = "imperial";
    // get "cnt" as number of days up to 16 days
    var daysTotal = 8;
  
    // start jQuery-based API Call
    $.get({
      url: weatherUrl + "&APPID=" + apiKey + "&units=" + unitType + "&cnt=" + daysTotal,
      success: function(objectFromOWM){
        getWeather(objectFromOWM);
       // console.log(objectFromOWM);
      },
      error: function(response){
        console.log(response);
      }
    });
  
  };
  
  // On button click, invoke APICall() and pass input text box value
  $('#getWeather').on('click', function(e){
  
    // prevent natural form submit event
    e.preventDefault();
    // check to see if search box has value
    if( $('#city-name').val().trim() === "" || $('#city-name').val().trim() === null ) {
      // if search box is empty, do nothing
      return;
    } else {
      //  clear old results
      $('.section').remove();
  
      // get input box value and invoke APICall function
      var cityName = $('#city-name').val().trim();
      $('#city-name').val("");
      APICall(cityName);
    }
  });
});