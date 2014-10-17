var app = angular.module('211ServicesApp', []);

// Jinja2 & Angular use the same things to designate templing,
// modify what is used.
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

// TabsController, controls navigation between different panes
app.controller('TabsController', function ($scope) {

    // Define the tabs and sections the user can toggle between
    $scope.tabs = [
        {
            title: 'Analytics',
            icon: 'fa-bar-chart',
            url: 'analytics.html'
        },
        {
            title: 'Database',
            icon: 'fa-search',
            url: 'database.html'
        },
        {
            title: 'Manage Users',
            icon: 'fa-user',
            url: 'manage-users.html'
        }
    ];

    // Begin on the analytics tab
    $scope.currentTab = 'analytics.html';

    // When a tab is clicked switch to that tab
    $scope.onClickTab = function(tab) {
        $scope.currentTab = tab.url;
    }

    // The active tab is the current tab
    $scope.isActiveTab = function(tabUrl) {
        return tabUrl == $scope.currentTab;
    }
});
