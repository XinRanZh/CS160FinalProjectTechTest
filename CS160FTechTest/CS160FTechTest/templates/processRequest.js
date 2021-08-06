function login(username, password) {
    console.log("456")
    var settings = {
        "url": "http://localhost:8000/login?username=" + username + "&" + "password=" + password,
        "method": "GET",
        "timeout": 0,
        "Access-Control-Allow-Origin":"*",
        headers: {
            "charset":"UTF-8",
            "Access-Control-Allow-Origin":'http://localhost:8080',
            "Access-Control-Allow-Credentials":"true",
          }
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}

function uploadText(filename, accessToken, text) {
    var settings = {
        "url": "http://localhost:8000/uploadText",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
          "fileName": filename,
          "accessToken": accessToken,
          "fileContent": text
        }
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}

function getText(filename) {
    var settings = {
        "url": "http://localhost:8000/getText?filename=" + filename,
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}