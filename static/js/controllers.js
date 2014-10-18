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
            url: 'static/analytics.html'
        },
        {
            title: 'Database',
            icon: 'fa-search',
            url: 'static/database.html'
        },
        {
            title: 'Manage Users',
            icon: 'fa-user',
            url: 'static/manage-users.html'
        }
    ];

    // Begin on the analytics tab
    $scope.currentTab = 'static/analytics.html';
    $('.contents').load($scope.currentTab);


    // When a tab is clicked switch to that tab
    $scope.onClickTab = function(tab) {
        if ($scope.currentTab !== tab.url) {
            $scope.currentTab = tab.url;
            // TODO(matthewe|2014): Fix this way of switching between things,
            // pretty sure there is a more angular way to do this
            $('.contents').load(tab.url).hide().fadeIn("slow");
        }
    }

    // The active tab is the current tab
    $scope.isActiveTab = function(tabUrl) {
        return tabUrl == $scope.currentTab;
    }
});
