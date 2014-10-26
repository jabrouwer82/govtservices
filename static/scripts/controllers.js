var app = angular.module('211ServicesApp', ['ngRoute', 'ngAnimate']);

// Jinja2 & Angular use the same things to designate templing,
// modify what is used for templating
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// Define the applications routing and controllers for each
app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/analytics', {
        templateUrl: 'static/views/analytics.html',
        controller: 'AnalyticsController'
    }).when('/database/:number?', {
        templateUrl: 'static/views/database.html',
        controller: 'DatabaseController'
    }).when('/manage-users', {
        templateUrl: 'static/views/manage-users.html',
        controller: 'ManageUsersController'
    }).when('/ask-watson', {
        templateUrl: 'static/views/ask-watson.html',
        controller: 'AskWatsonController'
    }).otherwise({
        redirectTo: '/analytics'
    })

}]);
