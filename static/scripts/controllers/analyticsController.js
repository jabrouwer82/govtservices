/** AnalyticsController -
 *
 * Defines the Analytics Controller. More coming soon..
 * Interacts with views/analytics.html
 */

angular.module('211ServicesApp').controller(
    'AnalyticsController',
    function ($scope) {

        $scope.selection = 1;

        $scope.data = {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [
                {
                    label: "My First dataset",
                    fillColor: "rgba(220,220,220,0.2)",
                    strokeColor: "rgba(220,220,220,1)",
                    pointColor: "rgba(220,220,220,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(220,220,220,1)",
                    data: [65, 59, 80, 81, 56, 55, 40]
                },
                {
                    label: "My Second dataset",
                    fillColor: "rgba(151,187,205,0.2)",
                    strokeColor: "rgba(151,187,205,1)",
                    pointColor: "rgba(151,187,205,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(151,187,205,1)",
                    data: [28, 48, 40, 19, 86, 27, 90]
                }
            ]
        };
        var options = {};


        $scope.myData = [
          { value : 50, color : "#2ecc71", label: 'Food' },
          { value : 90, color : "#e67e22", label: 'Shelter' },
          { value : 75, color : "#e74c3c", label: 'Clothing' },
          { value : 30, color : "#3498db", label: 'Job Resources'}
        ];
        $scope.myOptions = {};

    }
);
