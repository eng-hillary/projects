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
            color: H.getOptions().colors[0]
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
var R = Highcharts,
    resource_map = R.maps['countries/ug/ug-all'],
    chart;

Highcharts.getJSON('/resourcesharing/api/resource/', function (json) {
  var resource_data = [];
  json.forEach(function (r) {
      r.z = r.price;
      resource_data.push(r);
  })
//console.log(resource_data);
 
  chart = Highcharts.mapChart('resource_container', {
      title: {
          text: 'resource Locations'
      },
      
      mapNavigation: {
          enabled: true,
          buttonOptions: {
              verticalAlign: 'bottom'
          }
      },
     
      tooltip: {
          pointFormat: 'id: {point.id}<br>' +
              'resource_name: {point.resource_name}<br>' +
              'owner: {point.owner}<br>' +
              'price: {point.price}<br>' + 'shs'
    
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
          mapData: resource_map,
          borderColor: '#B0B0B0',
          nullColor: 'rgba(200, 200, 200, 0.2)',
          showInLegend: false
      }, {
          name: 'Separators',
          type: 'mapline',
          data: R.geojson(resource_map, 'mapline'),
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
          data: resource_data,
          maxSize: '5%',
          color: R.getOptions().colors[0]
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
  //Bar chart
  // Create the chart



var farmData =
[
    {
        "name": "piggery farm",
        "farmer": "karungi lydia",
        "lat": 0.37421,
        "lon": 32.64925,
        "land_occupied": 27.0
    },
    {
        "name": "poultry farm",
        "farmer": "musa rahim",
        "lat": 0.66367,
        "lon": 30.28204,
        "land_occupied": 42.0
    }
]

var districtData = [
    ['ug-2595', 0],
    ['ug-7073', 1],
    ['ug-7074', 2],
    ['ug-7075', 3],
    ['ug-2785', 4],
    ['ug-2791', 5],
    ['ug-3385', 6],
    ['ug-3388', 7],
    ['ug-2786', 8],
    ['ug-7056', 9],
    ['ug-7083', 10],
    ['ug-7084', 11],
    ['ug-7058', 12],
    ['ug-1678', 13],
    ['ug-1682', 14],
    ['ug-1683', 15],
    ['ug-1685', 16],
    ['ug-7051', 17],
    ['ug-2762', 18],
    ['ug-2767', 19],
    ['ug-2777', 20],
    ['ug-2778', 21],
    ['ug-2780', 22],
    ['ug-2781', 23],
    ['ug-2782', 24],
    ['ug-2783', 25],
    ['ug-2779', 26],
    ['ug-2784', 27],
    ['ug-3382', 28],
    ['ug-3384', 29],
    ['ug-3389', 30],
    ['ug-3383', 31],
    ['ug-3390', 32],
    ['ug-3386', 33],
    ['ug-3391', 34],
    ['ug-3392', 35],
    ['ug-3394', 36],
    ['ug-2750', 37],
    ['ug-7048', 38],
    ['ug-7080', 39],
    ['ug-7081', 40],
    ['ug-1684', 41],
    ['ug-7082', 42],
    ['ug-1688', 43],
    ['ug-7079', 44],
    ['ug-7068', 45],
    ['ug-7070', 46],
    ['ug-7049', 47],
    ['ug-2787', 48],
    ['ug-7055', 49],
    ['ug-2769', 50],
    ['ug-7052', 51],
    ['ug-2774', 52],
    ['ug-7059', 53],
    ['ug-7060', 54],
    ['ug-7057', 55],
    ['ug-2790', 56],
    ['ug-2776', 57],
    ['ug-7067', 58],
    ['ug-7065', 59],
    ['ug-7066', 60],
    ['ug-7069', 61],
    ['ug-7061', 62],
    ['ug-7063', 63],
    ['ug-7062', 64],
    ['ug-7064', 65],
    ['ug-7086', 66],
    ['ug-2744', 67],
    ['ug-1679', 68],
    ['ug-1680', 69],
    ['ug-7054', 70],
    ['ug-1686', 71],
    ['ug-7078', 72],
    ['ug-1677', 73],
    ['ug-1690', 74],
    ['ug-2745', 75],
    ['ug-2752', 76],
    ['ug-2754', 77],
    ['ug-1687', 78],
    ['ug-2757', 79],
    ['ug-1689', 80],
    ['ug-2760', 81],
    ['ug-2761', 82],
    ['ug-2766', 83],
    ['ug-2765', 84],
    ['ug-2764', 85],
    ['ug-2749', 86],
    ['ug-2768', 87],
    ['ug-2763', 88],
    ['ug-2748', 89],
    ['ug-2771', 90],
    ['ug-2772', 91],
    ['ug-2775', 92],
    ['ug-2788', 93],
    ['ug-2789', 94],
    ['ug-3381', 95],
    ['ug-3387', 96],
    ['ug-3393', 97],
    ['ug-7076', 98],
    ['ug-1681', 99],
    ['ug-2746', 100],
    ['ug-2747', 101],
    ['ug-2751', 102],
    ['ug-2758', 103],
    ['ug-2759', 104],
    ['ug-2756', 105],
    ['ug-2770', 106],
    ['ug-7072', 107],
    ['ug-7053', 108],
    ['ug-2753', 109],
    ['ug-2755', 110],
    ['ug-2773', 111]
];

//line gragh
//bar graph

// Create the chart

Highcharts.getJSON('/api-farmer/farmerprofiles/', function (json) {
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