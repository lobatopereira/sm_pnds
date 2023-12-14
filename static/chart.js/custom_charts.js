
  var $ChartSumariuPrograma  = $('#ChartSumariuPrograma');
  var $ChartStatusImplementasaunPrograma  = $('#ChartStatusImplementasaunPrograma');
  var $ChartImplementasaunProgramaArea  = $('#ChartImplementasaunProgramaArea');
  var $ChartImplementasaunProgramaYear  = $('#ChartImplementasaunProgramaYear');

  $.ajax({
        url: $ChartSumariuPrograma.data("url"),
        success: function (data) {
        var ctx = $ChartSumariuPrograma[0].getContext("2d");
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: data.labels,
                datasets: [
                {
                  data: data.data,
                  backgroundColor: ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462'],
                  hoverOffset: 4
                }
                ]
            },
            options: {
                plugins: {
                    datalabels: {
                        display: true
                    }
                }
            }
        })
        }
    });

  ////////////////////////////////////

  $.ajax({
      url: $ChartStatusImplementasaunPrograma.data("url"),
      success: function (data) {
        var ajaxdata = []
        for (let i in data.programLabels) {
            var totData = []
            for (let j in data.data) {
                totData.push(data.data[j][i])
            }
            ajaxdata.push(totData)
        }
        var backgroundColor = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462']
        var plotdata = []
        for (let i in ajaxdata) {
            plotdata.push({
                label: data.programLabels[i],
                data: ajaxdata[i],
                backgroundColor: backgroundColor[i],
                borderColor: backgroundColor[i],
                borderWidth: 1
            },)
        }
        var ctx = $ChartStatusImplementasaunPrograma[0].getContext("2d");

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: plotdata
        },
            options : {
              legend: {
                  display: true
              },
              scales: {
                yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      steps: 10,
                      stepValue: 5,
                      precision: 0
                  },
                  scaleLabel: {
                    display: true,
                    labelString: 'Total Implementasaun',
                  }
                }],
                xAxes: [{
                    scaleLabel: {
                      display: true,
                      labelString: "Status Implementasaun",
                    },
                  }]
              }
            }//end of options
    });
    }
    });

  ////////////////////////////////////
  ////////////////////////////////////

  $.ajax({
      url: $ChartImplementasaunProgramaArea.data("url"),
      success: function (data) {
        var ajaxdata = []
        for (let i in data.programLabels) {
            var totData = []
            for (let j in data.data) {
                totData.push(data.data[j][i])
            }
            ajaxdata.push(totData)
        }
        console.log(ajaxdata)
        var backgroundColor = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462']
        var plotdata = []
        for (let i in ajaxdata) {
            plotdata.push({
                label: data.programLabels[i],
                data: ajaxdata[i],
                backgroundColor: backgroundColor[i],
                borderColor: backgroundColor[i],
                borderWidth: 1
            },)
        }
        var ctx = $ChartImplementasaunProgramaArea[0].getContext("2d");

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: plotdata
        },
            options : {
              legend: {
                  display: true
              },
              scales: {
                yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      steps: 10,
                      stepValue: 5,
                      precision: 0
                  },
                  scaleLabel: {
                    display: true,
                    labelString: 'Total Implementasaun',
                  }
                }],
                xAxes: [{
                    scaleLabel: {
                      display: true,
                      labelString: "Area",
                    },
                  }]
              }
            }//end of options
    });
    }
    });

  ////////////////////////////////////
$.ajax({
      url: $ChartImplementasaunProgramaYear.data("url"),
      success: function (data) {
        var ajaxdata = []
        for (let i in data.programLabels) {
            var totData = []
            for (let j in data.data) {
                totData.push(data.data[j][i])
            }
            ajaxdata.push(totData)
        }
        console.log(ajaxdata)
        var backgroundColor = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462']
        var plotdata = []
        for (let i in ajaxdata) {
            plotdata.push({
                label: data.programLabels[i],
                data: ajaxdata[i],
                backgroundColor: backgroundColor[i],
                borderColor: backgroundColor[i],
                borderWidth: 1
            },)
        }
        var ctx = $ChartImplementasaunProgramaYear[0].getContext("2d");

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: plotdata
        },
            options : {
              legend: {
                  display: true
              },
              scales: {
                yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      steps: 10,
                      stepValue: 5,
                      precision: 0
                  },
                  scaleLabel: {
                    display: true,
                    labelString: 'Total Implementasaun',
                  }
                }],
                xAxes: [{
                    scaleLabel: {
                      display: true,
                      labelString: "Tinan",
                    },
                  }]
              }
            }//end of options
    });
    }
    });

  ////////////////////////////////////
