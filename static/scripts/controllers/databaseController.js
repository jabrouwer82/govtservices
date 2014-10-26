/** DatabaseController -
 *
 * Defines DatabaseController. More coming soon.
 * Interacts with views/database.html
 */

angular.module('211ServicesApp').controller(
    'DatabaseController',
    function ($scope, $http) {

        $scope.questions = [];

        // Only load the questions when this route is being viewed
        // http://stackoverflow.com/questions/15458609/angular-js-how-to-execute-function-on-page-load
        $scope.$on('$routeChangeSuccess', function() {
            $http.get('/api/questions').
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
);

