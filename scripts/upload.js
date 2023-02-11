var request = require('request');
var fs = require('fs');

async function upload(filepathPAN, filepathAadhar, userName){
    var options = {
    'method': 'POST',
    'url': 'https://app.zeeve.io/zdfs-api/api/v1/file/upload',
    'headers': {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjA3Yjc4OGNmN2U0NDYwOTAzYTRlZTRmODEzNWVkNjgyOGExMGIxOWUyNDFkYzU5NCIsImFjY291bnRfaWQiOiJmN2FkMjEwNy1iNmQ0LTRkMGUtODE5OS02OTBlNjJjMzk2NzciLCJhY2Nlc3Nfa2V5IjoiMDdiNzg4Y2Y3ZTQ0NjA5MDNhNGVlNGY4MTM1ZWQ2ODI4YTEwYjE5ZTI0MWRjNTk0IiwiZW1haWwiOiJ4YXJrMTEwM0BnbWFpbC5jb20iLCJpYXQiOjE2Njc4ODIzNzYsImV4cCI6MTk4MzQ1ODM3Nn0.fO1uDKCdvsou5KbcgiV_KFpkiZUwOWkvZ2-JkbeT_ek'
    },
    formData: {
        'files': fs.createReadStream(filepathPAN),
        'files': fs.createReadStream(filepathAadhar),
        'name': userName,
        'isDirectory': 'true'
    }
    };
    request(options, function (error, response) {
    if (error) throw new Error(error);
    var result = response.body
    var final = JSON.parse(result)
    console.log(final);
    var data = final.data;
    var fileID = data.fileID;
    return fileID;
});
}
// var aadharPath = "file-path-to-aadhar"
// var panPath = "file-path-to-pan"
// var userName = "test"
// var fileID = upload(aadharPath,panPath,userName);
// console.log(fileID)