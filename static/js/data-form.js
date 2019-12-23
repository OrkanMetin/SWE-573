var field;
var option;
var ex_options = 0;
function fields() {

    if( isNaN(field)) { field = 0; }
    field++;
    var fieldsDiv = document.getElementById('fields')
    var hiddenInputs = document.getElementById('hiddenInputs')
    var divtest = document.createElement("div");
	divtest.setAttribute("class", "form-group removeclass"+field);
    divtest.innerHTML = '<div class="row" style="width: 1000px">' +
        '<div class="col-sm-3 nopadding">' +
        '<div class="form-group">' +
        '<label for="InputName-'+field+'">Field Name</label>' +
        '<input type="text" class="form-control" id="InputName" aria-describedby="fieldName" placeholder="Enter Field Name" name="name">' +
        '</div> </div> <div class="col-sm-3 nopadding">' +
        '<div class="form-group"><label for="FormControlType">Type</label>' +
        '<select class="form-control" id="selectType'+ field +'" name="type">' +
        '<option>Text</option>' +
        '<option>Long Text</option>' +
        '<option>Integer</option>' +
        '<option>Decimal Number</option>' +
        '<option>Date</option>' +
        '<option>Time</option>' +
        '<option>Image</option>' +
        '<option>Video</option>' +
        '<option>Audio</option>' +
        '<option>Location</option>' +
        '</select>' +
        '</div>' +
        '</div>' +
        '<div class="col-sm-3 nopadding">' +
        '<div class="input-group">' +
        '<div class="form-group">' +
        '<label for="FormControlRequired">Required Field</label>' +
        '<select class="form-control" id="FormControlSelectRequired" name="required">' +
        '<option>Yes</option>' +
        '<option>No</option>' +
        '</select>' +
        '</div>' +
        '<div class="input-group-btn" style="top: 13px;">' +
        '<label for="FormControlRemoveField">' +
        '</label>' +
        '<button class="btn btn-danger" type="button" onclick="remove_fields('+ field +');">' +
        '<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>' +
        '</button>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '<div id="optionsField'+ field +'" class="optionsField'+ field +'" style="width: 1000px">' +
        '</div>' +
        '</div>';
    var hiddenInput = document.createElement("div");
    hiddenInput.setAttribute("class", "removeInput"+field);
    hiddenInput.innerHTML = '<input type="hidden" id="fieldId" name="fieldId" value='+ field +'>';
    fieldsDiv.appendChild(divtest)
    hiddenInputs.appendChild(hiddenInput)
}

function remove_fields(fieldid) {
    var field_id = parseInt(fieldid);
    $('.removeclass'+field_id).remove();
    $('.removeInput'+field_id).remove();
}

function addOption(fieldid){
    var field_id = parseInt(fieldid);
    option++;
    var objTo = document.getElementById('optionsField'+field_id);
    var divtest = document.createElement("div");
    divtest.setAttribute("class", "form-group option"+option);
    divtest.innerHTML = '<div style="width: 250px; margin-left: 50px;">' +
        '<div class="input-group"><div class="form-group">' +
        '<input type="text" class="form-control" id="InputOption" aria-describedby="option" placeholder="Enter an option" name="option'+ field_id +'">' +
        '</div>' +
        '<div class="input-group-btn">' +
        '<label for="FormControlRemoveField">' +
        '</label>' +
        '<button class="btn btn-danger" type="button" onclick="removeOption('+ option +');">' +
        '<span class="glyphicon glyphicon-minus" aria-hidden="true">' +
        '</span>' +
        '</button>' +
        '</div>' +
        '</div>' +
        '</div>';
    objTo.appendChild(divtest)
}

function removeOption(optionid) {
    var option_id = parseInt(optionid);
    $('.option'+option_id).remove();
}

