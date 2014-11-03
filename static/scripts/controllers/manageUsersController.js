/** ManageUsersController
 *
 * Defines interaction to just ask Watson a question and get
 * answer back in a formatted way.
 */
angular.module('211ServicesApp').controller(
    'ManageUsersController',
    function ($scope, $http, $timeout) {

        // TODO(matthewe|2014-10-20): Hook this up to the API
        $http.get('api/usersl').success(function(data, status, headers, config){
            $scope.users = data;}).
        error(function(data){
            $scope.users = [{
                name: 'Matthew Ebeweber',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Bri Connelly',
                company: 'United Way',
                title: 'Manager'
            }]
        });

        $scope.submitUser = function(){
            $scope.toggle = !$scope.toggle;
            newUser = $scope.User;
            $scope.users.push(newUser);
            $scope.User = {};
            $scope.add-user-form.$setPristine();
        }
    }

);
