{{cookiecutter.project_slug|title}}.Base.User = (function ($) {
    var options = {
        Debug: false,
    }

    var initialize = function (args) {
        $.extend(options, args);
    }

    return {
        Initialize: initialize,
        Options: options,

    };
}(jQuery));
