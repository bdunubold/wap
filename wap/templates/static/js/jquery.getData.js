    // Data retrieval for Plotting statstical data.

    var m = [];
    var arr_movies = [];

// Ploting pie chart
    $.ajax({
        url: '/movie/latest/',
        type: 'GET',
        dataType: 'json'
    }).done(function (result) {
        console.log(result);
        $.each(result, function (i, movie) {

       arr_movies.push(movie.fields.category);

        });

        var arr;
         // the number of each category in the movie pool
        function count(arr) {
            return arr.reduce((prev, curr) => (prev[curr] = ++prev[curr] || 1, prev), {})
        }

        console.log(count(arr_movies));
        var dataset = count(arr_movies);


       Highcharts.chart('piechart', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Distribution of movies by Category'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Category',
            colorByPoint: true,
            data: [{
                name: Object.keys(dataset)[0],
                y: dataset[Object.keys(dataset)[0]]

            }, {
                 name: Object.keys(dataset)[1],
                y: dataset[Object.keys(dataset)[1]]

            }, {
                name: Object.keys(dataset)[2],
                y: dataset[Object.keys(dataset)[2]]
            }, {
                name: Object.keys(dataset)[3],
                y: dataset[Object.keys(dataset)[3]]
            }, {
                name: Object.keys(dataset)[4],
                y: dataset[Object.keys(dataset)[4]]
            }]
        }]




    });

    })
        .fail(function (xhr, status, err) {
            console.log(status);
        })
        .always(function (xhr, status) {
            console.log(status);
        });


// Plot bar chart for the number of views
    $.ajax({
        url: '/screening/list/',
        type: 'GET',
        dataType: 'json'
    }).done(function (result) {
        console.log(result);

        var arr;
        var movie_title = [];
        $.each(result, function (j, screen) {

            m.push(screen.fields.movie);
            // movie_title.push(screen.fields.title);

        });

        // Count the number of views for each movie
        function count(arr) {
            return arr.reduce((prev, curr) => (prev[curr] = ++prev[curr] || 1, prev), {})
        }

        var y = count(m)
        console.log(y);


        for(var i=0; i<100; i++){

             movie_title[i] = "Title"+i;
        }

        Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Number of Views per movie'
        },

        xAxis: {
            categories: [ movie_title[0], movie_title[1],
                            movie_title[2], movie_title[3], movie_title[4]],
            title: {
                text: 'Movie Title'
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of Times Watched',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },

        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },

        credits: {
            enabled: false
        },
        series: [{
            name: 'First five movies',
            data: [y[Object.keys(y)[0]], y[Object.keys(y)[1]], y[Object.keys(y)[2]],
                    y[Object.keys(y)[3]], y[Object.keys(y)[4]]]
        }]
   });


        })
        .fail(function (xhr, status, err) {
            console.log(status);
        })
        .always(function (xhr, status) {
            console.log(status);
        });




