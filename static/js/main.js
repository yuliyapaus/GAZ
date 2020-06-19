jQuery("document").ready(function () {

});

// ФУНКЦИИ ДЛЯ ПЛАНИРОВАНИЯ

// ФУНКЦИИ ДЛЯ РЕЕСТРА ДОГОВОРОВ

// ФУНКЦИИ ДЛЯ АНАЛИТИКИ

// ФУНКЦИИ ДЛЯ АДМИНИСТРИРОВАНИЯ

// ФУНКЦИИ ДЛЯ СПРАВОЧНИКОВ

function enableEditMode() {
    $('main #td-edit-mode').css('display', 'table-cell');
    $('main #btn-edit-mode-show').css('display', 'inline-block');
    $('main #btn-edit-mode-hide').css('display', 'none');
}

function saveEditions() {
    $('main #td-edit-mode').css('display', 'none');
    $('main #btn-edit-mode-show').css('display', 'none');
    $('main #btn-edit-mode-hide').css('display', 'inline-block');
}

// ФУНКЦИИ ДЛЯ УВЕДОМЛЕНИЙ
