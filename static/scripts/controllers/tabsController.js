/** TabsController -
 *
 * Defines the different tabs (navigation) displayed on the
 * web application and interaction.
 */

angular.module('211ServicesApp').controller(
    'TabsController',
    function ($scope, $location) {

        /** List of tabs to be displayed, currently requires
        title, url, activeUrl and icon. Icons can be found on:
        http://fortawesome.github.io/Font-Awesome/icons/
        */
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

        /**
        @function isActive Returns boolean indicating if tab is active
        @param {String} route - the current active route
        */
        $scope.isActive = function(route) {
            // TOOD(matthewe|2014-10-26): This is pretty ugly,
            // rewrite the way we detect active tabs
            return route.split("/")[1] === $location.path().split("/")[1];
        }
    }
);
