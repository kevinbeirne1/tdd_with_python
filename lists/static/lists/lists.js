window.Superlists = {}
window.Superlists.initialize = function () {
        $('input[name="text"]').on('keypress', () => {
            $('.has-error').hide()
        });

        $('input[name="text"]').on('click', () => {
            $('.has-error').hide()
        });

};

