var app = angular.module('211ServicesApp', ['ngRoute', 'ngAnimate']);

// Jinja2 & Angular use the same things to designate templing,
// modify what is used.
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

// Define the applications routing and controllers for each
app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/analytics', {
        templateUrl: 'views/analytics.html',
        controller: 'AnalyticsController'
    }).when('/database', {
        templateUrl: 'views/database.html',
        controller: 'DatabaseController'
    }).when('/manage-users', {
        templateUrl: 'views/manage-users.html',
        controller: 'ManageUsersController'
    }).when('/ask-watson', {
        templateUrl: 'views/ask-watson.html',
        controller: 'AskWatsonController'
    }).otherwise({
        redirectTo: '/analytics'
    })

}]);

// TabsController, controls navigation between different panes
app.controller('TabsController', function ($scope, $location) {

    // Define the tabs and sections the user can toggle between
    $scope.tabs = [
        {
            title: "Analytics",
            url: '#analytics',
            activeUrl: '/analytics',
            icon: 'fa-bar-chart'
        },
        {
            title: "Database",
            url: '#database',
            activeUrl: '/database',
            icon: 'fa-search'
        },
        {
            title: "Manage Users",
            url: '#manage-users',
            activeUrl: '/manage-users',
            icon: 'fa-user'
        },
        {
            title: "Ask Watson",
            url: '#ask-watson',
            activeUrl: '/ask-watson',
            icon: 'fa-globe'
        }
    ];

    $scope.isActive = function(route) {
        return route === $location.path();
    }
});

app.controller('AnalyticsController', function ($scope) {
    $scope.title = 'AnalyticsController';
})

app.controller('DatabaseController', function ($scope) {
    $scope.title = 'DatabaseController';
})

// TODO(matthewe|10-20-2014): Clean this up and the
// ManageUserscontroller, separate this file into different
// components
app.controller('ManageUsersController', function ($scope, $timeout) {
    // TODO(matthewe|2014-10-20): This should come from an API
    // call rather than being static. Endpoint needs to be set
    // up
    $scope.sponsors = [];
    $timeout(function() {
        $scope.sponsors = [
            {
                name: 'Matt Ebeweber',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Bri Connelly',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Sai Avala',
                company: 'United Way',
                title: 'Caller'
            },
            {
                name: 'Sai Avala',
                company: 'United Way',
                title: 'Caller'
            },
            {
                name: 'Matt Ebeweber',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Bri Connelly',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Sai Avala',
                company: 'United Way',
                title: 'Caller'
            },
            {
                name: 'Sai Avala',
                company: 'United Way',
                title: 'Caller'
            },
            {
                name: 'Matt Ebeweber',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Bri Connelly',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Sai Avala',
                company: 'United Way',
                title: 'Caller'
            },
            {
                name: 'Sai Avala',
                company: 'United Way',
                title: 'Caller'
            }
        ];
    });
})

app.controller('AskWatsonController', function ($scope, $http) {
    $scope.searchQuestion = "";
    $scope.loading = false;

    $scope.askQuestion = function() {
        $scope.loading = true;

        $http.get('/ask', {
            question: 'things things and more things'
        }).success(function(data, status, headers, config) {
            scope.loading = false;
        }).error(function(data, status, headers, config) {
            // TODO(matthewe|2014-10-17): Handle the error
            $scope.loading = false;
        });
    };
})
