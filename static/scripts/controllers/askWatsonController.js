/** AskWatsonController
 *
 * Defines interaction to just ask Watson a question and get
 * answer back in a formatted way.
 */

angular.module('211ServicesApp').controller(
    'AskWatsonController',
    function ($scope, $http) {
        $scope.searchQuestion = "";
        $scope.loading = false;

        $scope.askQuestion = function() {
            $scope.loading = true;
            $scope.results = null;

            $http.get('/api/ask', {
                params: {
                    q: $scope.searchQuestion,
                    z: 1, l: 1, p: 0
                }
            }).success(function(data, status, headers, config) {
                $scope.loading = false;
                $scope.results = data;
            }).error(function(data, status, headers, config) {
                // TODO(matthewe|2014-10-17): Handle the error
                $scope.loading = false;
                $scope.results = data;
            });
        };
    }
);
