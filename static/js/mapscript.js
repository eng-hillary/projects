//map
var data = [
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

// Create the chart
Highcharts.mapChart('container', {
    chart: {
        map: 'countries/ug/ug-all'
    },

    title: {
        text: 'Farmer Locations'
    },

    subtitle: {
        text: 'Source map: <a href="https://code.highcharts.com/mapdata/countries/ug/ug-all.js">Uganda</a>'
    },

    mapNavigation: {
        enabled: true,
        buttonOptions: {
            verticalAlign: 'bottom'
        }
    },

    colorAxis: {
        min: 0
    },

    series: [{
        data: data,
        name: 'Random data',
        states: {
            hover: {
                color: ' #228B22'
            }
        },
        dataLabels: {
            enabled: true,
            format: '{point.name}'
        }
    }]
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
      name: 'Brands',
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
Highcharts.chart('barcontainer', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Coffee Growers Percentage in sample by July, 2020'
    },
    subtitle: {
        text: ''
    },
    accessibility: {
        announceNewData: {
            enabled: true
        }
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        title: {
            text: 'Total percent market share'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}%'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
    },

    series: [
        {
            name: "Browsers",
            colorByPoint: true,
            data: [
                {
                    name: "Bushenyi",
                    y: 62.74,
                    drilldown: "Bushenyi"
                },
                {
                    name: "Sheema",
                    y: 10.57,
                    drilldown: "Sheema"
                },
                {
                    name: "Arua",
                    y: 7.23,
                    drilldown: "Arua"
                },
                {
                    name: "Apac",
                    y: 5.58,
                    drilldown: "Apac"
                },
                {
                    name: "Kitgum",
                    y: 4.02,
                    drilldown: "Kitgum"
                },
                {
                    name: "Kololo",
                    y: 1.92,
                    drilldown: "Kololo"
                },
                {
                    name: "Others",
                    y: 7.62,
                    drilldown: null
                }
            ]
        }
    ],
    drilldown: {
        series: [
            {
                name: "Bushenyi",
                id: "Bushenyi",
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
                name: "Sheema",
                id: "Sheema",
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
                name: "Arua",
                id: "Arua",
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
                name: "Apac",
                id: "Apac",
                data: [
                    [
                        "v11.0",
                        3.39
                    ],
                    [
                        "v10.1",
                        0.96
                    ],
                    [
                        "v10.0",
                        0.36
                    ],
                    [
                        "v9.1",
                        0.54
                    ],
                    [
                        "v9.0",
                        0.13
                    ],
                    [
                        "v5.1",
                        0.2
                    ]
                ]
            },
            {
                name: "Kitgum",
                id: "Kitgum",
                data: [
                    [
                        "v16",
                        2.6
                    ],
                    [
                        "v15",
                        0.92
                    ],
                    [
                        "v14",
                        0.4
                    ],
                    [
                        "v13",
                        0.1
                    ]
                ]
            },
            {
                name: "Kololo",
                id: "Kololo",
                data: [
                    [
                        "v50.0",
                        0.96
                    ],
                    [
                        "v49.0",
                        0.82
                    ],
                    [
                        "v12.1",
                        0.14
                    ]
                ]
            }
        ]
    }
});
