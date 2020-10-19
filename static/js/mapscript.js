//map showing farms
var H = Highcharts,
    map = H.maps['countries/ug/ug-all'],
    chart;

Highcharts.getJSON('/farm/api/maps/', function (json) {
    var data = [];
    json.forEach(function (p) {
        p.z = p.land_occupied;
        data.push(p);
    })

// console.log(data)  
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
        }]
    });
});


// Display custom label with lat/lon next to crosshairs
document.getElementById('farm_container').addEventListener('mousemove', function (e) {
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


document.getElementById('farm_container').addEventListener('mouseout', function () {
    if (chart && chart.lab) {
        chart.lab.destroy();
        chart.lab = null;
    }
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