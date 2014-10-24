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

            $http.get('/ask', {
                question: 'things things and more things'
            }).success(function(data, status, headers, config) {
                scope.loading = false;
            }).error(function(data, status, headers, config) {
                // TODO(matthewe|2014-10-17): Handle the error
                $scope.loading = false;
            });
        };
    }
);
