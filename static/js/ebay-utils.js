/**
 * Created by olunx on 15/1/9.
 */

function formValidate() {
    var form = $('#main-form');
    form.data('bootstrapValidator').validate();
    if (!form.data('bootstrapValidator').isValid()) {
        $.niftyNoty({
            type: 'danger',
            container: 'page',
            html: '<strong><li class="fa fa-frown-o"></li> 操作失败!</strong> 请检查标红的内容！',
            timer: 10000
        });
        return false;
    }
    return true;
}

function formData() {
    $('#summernote').val($('#summernote').code());
    var data = $('#main-form').serializeJSON();

    //未选择的图片
    var images = new Array();
    $.each($('input[rel="images"]:not(:checked)'), function () {
        images.push($(this).val());
    });
    data['images'] = JSON.stringify(images);

    //已选择的图片
    var images_checked = new Array();
    $.each($('input[rel="images"]:checked'), function () {
        images_checked.push($(this).val());
    });
    data['images_checked'] = JSON.stringify(images_checked);
    return data;
}

function translateContent() {
    var text = $('#summernote').code();
    ajaxPost('/api/translate/', {'text': text, 'lang': 'en'}, function (response) {
        $('#summernote').code(response.result);
    });
}

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
                    greaterThan: {
                        value: 1,
                        message: 'The value must be greater than 0'
                    }
                }
            },
            price: {
                validators: {
                    notEmpty: {
                        message: 'The value is required and can\'t be empty'
                    },
                    greaterThan: {
                        value: 0.01,
                        message: 'The price must be greater than 0.01'
                    }
                }
            },
            item_postal: {
                validators: {
                    integer: {
                        message: 'The value must larger than 0'
                    }
                }
            }
        }
    }).on('err.form.fv', function (e, data) {
        // $(e.target)  --> The field element
        // data.bv      --> The BootstrapValidator instance
        // data.field   --> The field name
        // data.element --> The field element
        var $parent = data.element.parents('.form-group');

        // Remove the has-success class
        $parent.removeClass('has-success');
    });
});