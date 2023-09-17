function authme() {
    let response_uname = prompt('Who are you?', 'Enter your userid');
    if (response_uname == "iamdeb") {
        var authenticated = false;
        while (authenticated == false) {
            let response_pswd = prompt(`Hello ${response_uname}`, `Enter your password`);
            if (response_pswd != "123") {
                alert("Wrong passcode ... please try again !!");
            }
            else {
                alert(`Welcome ${response_uname}`);
                authenticated = true;
                document.getElementById("xyz").style.display = 'block';
            }
        }
    }
    else {
        authme();
    }
}