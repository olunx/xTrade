/**
 * Created by olunx on 15/1/9.
 */

$(document).ready(function () {

    // Feedback Icons
    // =================================================================
    var faIcon = {
        valid: 'fa fa-check-circle fa-lg text-success',
        invalid: 'fa fa-times-circle fa-lg',
        validating: 'fa fa-refresh'
    }

    // Validators
    // =================================================================
    $('#main-form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: faIcon,
        fields: {
            account: {
                validators: {
                    choice: {
                        min: 1,
                        max: 1,
                        message: 'Please choose the ebay account.'
                    }
                }
            },
            title: {
                message: 'The title is not valid',
                validators: {
                    notEmpty: {
                        message: 'The title is required.'
                    },
                    stringLength: {
                        min: 10,
                        max: 80
                    }
                }
            },
            item_location: {
                validators: {
                    notEmpty: {
                        message: 'The country is required and can\'t be empty'
                    }
                }
            },
            quality: {
                validators: {
                    notEmpty: {
                        message: 'The quality is required and can\'t be empty'
                    },
                    integer: {
                        message: 'The value is not a number'
                    }
                }
            },
            price: {
                validators: {
                    notEmpty: {
                        message: 'The price is required and can\'t be empty'
                    },
                    numeric: {
                        message: 'The value is not a number'
                    }
                }
            },
            item_postal: {
                validators: {
                    integer: {
                        message: 'The value is not a number'
                    }
                }
            }
        }
    }).on('success.field.bv', function (e, data) {
        // $(e.target)  --> The field element
        // data.bv      --> The BootstrapValidator instance
        // data.field   --> The field name
        // data.element --> The field element

        var $parent = data.element.parents('.form-group');

        // Remove the has-success class
        $parent.removeClass('has-success');
    });
});