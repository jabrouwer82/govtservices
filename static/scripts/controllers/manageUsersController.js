/** ManageUsersController
 *
 * Defines interaction to just ask Watson a question and get
 * answer back in a formatted way.
 */
angular.module('211ServicesApp').controller(
    'ManageUsersController',
    function ($scope, $timeout) {
        // TODO(matthewe|2014-10-20): Hook this up to the API
        $scope.users = [
            {
                name: 'Matt Ebeweber',
                company: 'United Way',
                title: 'Manager'
            },
            {
                name: 'Bri Connelly',
                company: 'United Way',
                title: 'Manager'
            }
        ];
    }
);
