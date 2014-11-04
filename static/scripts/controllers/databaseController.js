/** DatabaseController -
 *
 * Defines DatabaseController. More coming soon.
 * Interacts with views/database.html
 */

angular.module('211ServicesApp').controller(
    'DatabaseController',
    function ($scope, $http, $routeParams) {
        $scope.number = $routeParams.number;

        // Two different work flows depending on whether or not number
        // is defined. One for general view and one for a much more
        // specific view.
        if ($scope.number) {
            // Pull down information for specific phone number
            $scope.$on('$routeChangeSuccess', function() {
                $http.get('/api/questions/phone_number', {
                    params: {
                        'p': parseInt($scope.number),
                        'z': 1
                    }
                }).
                success(function(data, status, headers, config) {
                    $scope.askedQuestions = data.questions;
                }).
                error(function(data, status, headers, config) {
                    // TODO(matthewe|2014-10-26): You should probably
                    // handle a failed request in some way (sweetAlert?)
                    console.log('/api/questions failed');
                });
            });
        } else {
            // Pull down general information
            $scope.questions = [];

            // Only load the questions when this route is being viewed
            // http://stackoverflow.com/questions/15458609/angular-js-how-to-execute-function-on-page-load
            $scope.$on('$routeChangeSuccess', function() {
                $http.get('/api/questions', {
                    params: {
                        'z': 1
                    }
                }).
                success(function(data, status, headers, config) {
                    $scope.questions = data;
                }).
                error(function(data, status, headers, config) {
                    // TODO(matthewe|2014-10-26): You should probably
                    // handle a failed request in some way (sweetAlert?)
                    console.log('/api/questions failed');
                });
            });
        }
    }
);

