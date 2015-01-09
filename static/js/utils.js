/**
 * Created by olunx on 15/1/9.
 */

function pack_data(){
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