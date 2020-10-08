var H = Highcharts,
    map = H.maps['countries/ug/ug-all'],
    chart;

// Add series with state capital bubbles
Highcharts.getJSON('/farm/api/maps/', function (json) {
    var data = [];
    json.forEach(function (p) {
        p.z = p.land_occupied;
        data.push(p);
    })


//console.log(data);
    chart = Highcharts.mapChart('container', {
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
            pointFormat: 'district: {point.district}<br>' +
                'farmer: {point.farmer}<br>' +
                'farm name: {point.farm_name}<br>' +
                'latittude: {point.lat}<br>' +
                'longitude: {point.lon}<br>'+ 
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
document.getElementById('container').addEventListener('mousemove', function (e) {
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

document.getElementById('container').addEventListener('mouseout', function () {
    if (chart && chart.lab) {
        chart.lab.destroy();
        chart.lab = null;
    }
});



//Piechart Js
Highcharts.chart('piecontainer', {
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: 'pie'
    },
    title: {
      text: 'Coffee Growers Percentage in sample by July, 2020'
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
      point: {
        valueSuffix: '%'
      }
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '<b>{point.name}</b>: {point.percentage:.1f} %'
        }
      }
    },
    series: [{
      name: 'Districts',
      colorByPoint: true,
      data: [{
        name: 'Chrome',
        y: 61.41,
        sliced: true,
        selected: true
      }, {
        name: 'Bushenyi',
        y: 11.84
      }, {
        name: 'Sheema',
        y: 10.85
      }, {
        name: 'Arua',
        y: 4.67
      }, {
        name: 'Rukungiri',
        y: 4.18
      }, {
        name: 'Apac',
        y: 1.64
      }, {
        name: 'Kalangala',
        y: 1.6
      }, {
        name: 'Moroto',
        y: 1.2
      }, {
        name: 'Others',
        y: 2.61
      }]
    }]
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
